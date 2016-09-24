__all__ = ['app_config']

import sys, os, os.path
try: import ConfigParser as configparser
except ImportError: import configparser

try: import simplejson as json
except ImportError: import json

from .base_utils import *

class AppConfig(configparser.RawConfigParser):
    config_filename = 'my-app.ini'
    main_section = 'MyApp'
    def __init__(self, *args, **kw):
        configparser.RawConfigParser.__init__(self, *args, **kw)
        self.base_dir = base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.read(os.path.join(self.base_dir, self.config_filename))
        self.log_level = self.opt_string(self.main_section, 'log-level', 'info').strip().upper()
        self.is_debug = self.log_level=='DEBUG'

    def opt_string(self, section, key, fallback=None):
        return self.get(section, key) if self.has_option(section, key) else fallback
    
    def opt_int(self, section, key, fallback=0):
        return try_int(self.opt_string(section, key, str(fallback)), fallback)

app_config=AppConfig()
