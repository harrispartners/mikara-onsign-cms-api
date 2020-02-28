import json

from src.entity.player import Player
from src.entity.pageinfo import PageInfo


class PlayerConnection:
    nodes = None
    pageInfo = None
    totalCount = None
    
    
    def __init__(self,
                 nodes=None,
                 pageInfo=None,
                 totalCount=None):
        if nodes:
            self.nodes = [Player(**x) for x in nodes]
        
        if pageInfo:
            self.pageInfo = PageInfo(**pageInfo)
        
        if totalCount:
            self.totalCount = totalCount
    
    
    @staticmethod
    def parse(json_data):
        if type(json_data) is str:
            json_data = json.loads(json_data)   # Create into a json dict if it's not
        
        json_data = json_data['data']['organization']['players']
        
        return PlayerConnection(**json_data)