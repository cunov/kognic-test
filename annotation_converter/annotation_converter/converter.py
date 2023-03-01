"""

"""
# Futures

# Built-in/Generic Imports

# Libs
import requests
# Own modules
from . import module
__author__ = 'Colton Cunov'
__email__ = 'colton.cunov@nevs.com'
__created__ = '2023-02-28 14:58:32'
__credits__ = '{{ credit_list }}'
__version__ = '0.0.1'
__maintainer__ = 'Colton Cunov'
__status__ = 'Under Dev'


def convert(annotation: dict):
    url = module.base_url + 'conversion'
    resp = requests.get(url, json=annotation)
    return resp.json()