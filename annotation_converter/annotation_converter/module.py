"""

"""
# Futures

# Built-in/Generic Imports
import sys
import os
# Libs

# Own modules
from . import params

__author__ = 'Colton Cunov'
__email__ = 'colton.cunov@nevs.com'
__created__ = '2023-03-01 10:01:02'
__credits__ = '{{ credit_list }}'
__version__ = '0.0.1'
__maintainer__ = 'Colton Cunov'
__status__ = 'Under Dev'


class This(sys.__class__):
    _host = params.HOST
    _port = params.PORT
    _num_tries = params.NUM_TRIES
    _base_url = params.BASE_URL
    _template_file = params.TEMPLATE_FILE

    @property
    def host(self):
        return self._host
    
    @host.setter
    def host(self, host):
        self._host = host
        self._base_url = f'http://{self._host}:{self._port}/'

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        self._base_url = base_url

    @property
    def port(self):
        return self._port
    
    @port.setter
    def port(self, port):
        self._port = port
        self._base_url = f'http://{self._host}:{self._port}/'

    @property
    def template_file(self):
        if not os.path.exists(self._template_file):
            raise FileNotFoundError(f'{self._template_file} does not exist. Did you forget to set it?')
        return self._template_file
    
    @template_file.setter
    def template_file(self, template_file):
        if not os.path.exists(template_file):
            raise FileNotFoundError(f'{template_file} does not exist')
        self._template_file = template_file

    @property
    def num_tries(self):
        return self._num_tries
    
    @num_tries.setter
    def num_tries(self, num_tries):
        self._num_tries = num_tries
    

sys.modules[__name__].__class__ = This