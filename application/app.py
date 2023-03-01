"""

"""
# Futures

# Built-in/Generic Imports
import json
# Libs
from flask import Flask, request
# Own modules
from annotation_converter.module import template_file

__author__ = 'Colton Cunov'
__email__ = 'colton.cunov@nevs.com'
__created__ = '2023-02-28 15:05:34'
__credits__ = '{{ credit_list }}'
__version__ = '0.0.1'
__maintainer__ = 'Colton Cunov'
__status__ = 'Under Dev'

class Object:
    def __init__(self, id_, obj_type, dict):
        self.id_ = id_
        self.class_ = obj_type
        self.params = dict

    def add_bbox(self, dict):
        self.bbox = dict

    def convert_bbox(self):
        min_x, max_x = self.bbox['min_x'], self.bbox['max_x']
        min_y, max_y = self.bbox['min_y'], self.bbox['max_y']
        x_center = min_x + (max_x - min_x) / 2
        y_center = min_y + (max_y - min_y) / 2
        width = max_x - min_x
        height = max_y - min_y
        return [x_center, y_center, width, height]
    
    def get_header_dict(self):
        return {'name':self.id_, 'type': self.class_}
    
    def get_object_dict(self):
        object_data = {
            'bbox': [
                {
                    'name': self.bbox['name'],
                    'stream': self.bbox['stream'],
                    'val': self.convert_bbox()
                }
            ]
        }
        for key,val in self.params.items():
            if isinstance(val, str):
                if not 'text' in object_data:
                    object_data['text'] = []
                object_data['text'].append({'name':key, 'val':val})
            elif isinstance(val, bool):
                if not 'boolean' in object_data:
                    object_data['boolean'] = []
                object_data['boolean'].append({'name':key, 'val':val})
        return object_data
        
    

def convert_annotation(annotation: dict):
    """
    Ideally we would have an intermediate/core representation which we could
    convert to/from any other representation. Not sure if that's feasible
    since idk what the other representations look like, but seems like there
    could be a lot of pairs without much overlap.

    If not, then a factory is the best way to go about it.
    """
    objs = {}
    for id_, dic in annotation['shapeProperties'].items():
        dic = dic['@all']
        obj_class = dic['class']
        del dic['class']
        objs[id_] = Object(id_, obj_class, dic)

    for stream in annotation['shapes']:
        for feature in annotation['shapes'][stream]['features']:
            id_ = feature['id']
            assert id_ in objs
            # asserting within a running service is ungood
            # but at least you know I thought about that case
            
            bbox_dict = {}
            bbox_dict['name'] = f'bbox-{id_[:id_.find("-")]}'
            bbox = [tuple(dic['coordinates']) for dic in feature['geometry']['coordinates'].values()]
            x_vals, y_vals = [tup[0] for tup in bbox], [tup[1] for tup in bbox]
            bbox_dict['max_x'], bbox_dict['min_x'] = max(x_vals), min(x_vals)
            bbox_dict['max_y'], bbox_dict['min_y'] =max(y_vals), min(y_vals)
            bbox_dict['stream'] = stream
            objs[id_].add_bbox(bbox_dict)


    header_dict = {}
    objects_dict = {}
    for obj in objs.values():
        header_dict[obj.id_] = obj.get_header_dict()
        objects_dict[obj.id_] = obj.get_object_dict()

    with open(template_file, 'r') as f:
        openlabel_dict = json.load(f)
    openlabel_dict['data']['openlabel']['objects'] = header_dict
    # assuming not enough info to infer the frame # or configs
    openlabel_dict['data']['openlabel']['frames']['0']['objects'] = objects_dict

    return json.dumps(openlabel_dict)


def create_app():
    app = Flask(__name__)

    @app.get('/conversion')
    def conversion():
        if request.is_json:
            kognic_annot = request.get_json()
            return convert_annotation(kognic_annot), 201
        return {'Error': 'Request payload must be json'}, 415
    
    @app.get('/test')
    def test():
        return 'App is responding', 200
    
    return app