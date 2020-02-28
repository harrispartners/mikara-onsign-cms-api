import json

from src.entity.playlist import Playlist
from src.entity.pageinfo import PageInfo


class PlaylistConnection:
    nodes = None
    pageInfo = None
    totalCount = None
    
    
    def __init__(self,
                 nodes=None,
                 pageInfo=None,
                 totalCount=None):
        if nodes:
            self.nodes = [Playlist(**x) for x in nodes]
        
        if pageInfo:
            self.pageInfo = PageInfo(**pageInfo)
        
        if totalCount:
            self.totalCount = totalCount
    
    
    @staticmethod
    def parse(json_data):
        if json_data is None:
            return None
        
        if type(json_data) is str:
            json_data = json.loads(json_data)
        
        json_data = json_data['data']['organization']['playlists']
        
        return PlaylistConnection(**json_data)