import json

from src.utils import *


class Organization:
    id = None
    name = None
    
    
    def __init__(self,
                 id,
                 name=None):
        
        self.id = id
        self.name = name
        
        
    @staticmethod
    def parse(json_data):
        if type(json_data) is str:
            json_data = json.loads(json_data)   # Create into a json dict if it's not
        
        json_data = json_data['data']['organization']
        
        return Organization(**json_data)