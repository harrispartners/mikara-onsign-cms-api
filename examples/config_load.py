import configparser
import os
import sys


class ConfigLoad:
    config = None

    def __init__(self):
        sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

        if self.config is None:
            self.config = configparser.ConfigParser()
            dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file = dir + '/settings.py'
            self.config.read(file)

    def get(self, key):
        return self.config['DEFAULT'][key]
