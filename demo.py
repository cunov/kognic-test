"""

"""
# Futures

# Built-in/Generic Imports
import json
# Libs

# Own modules
from annotation_converter import convert
# import annotation_converter
# annotation_converter.module.template_file = 'application/open_label.txt'

__author__ = 'Colton Cunov'
__email__ = 'colton.cunov@kognic.com'
__created__ = '2023-02-28 13:41:11'
__credits__ = '{{ credit_list }}'
__version__ = '0.0.1'
__maintainer__ = 'Colton Cunov'
__status__ = 'Under Dev'

if __name__ == '__main__':
    path_to_kognic_annotation = 'kognic_1.json'
    with open(path_to_kognic_annotation, 'r') as content:
        kognic_annotation = json.load(content)

    open_label_annotation = convert(kognic_annotation)
    with open('open_label_generated.json','w+') as f:
        json.dump(open_label_annotation, f, indent=2)
    print(open_label_annotation)
