from src.entity.playlistitem import PlaylistItem
from src.entity.pageinfo import PageInfo
from src.utils import *


class PlaylistItemConnection:
    edges = None
    pageInfo = None
    totalCount = None
    
    
    def __init__(self,
                 edges=None,
                 pageInfo=None,
                 totalCount=None):
        self.edges = from_json_list(edges, PlaylistItem)
        self.pageInfo = from_json(pageInfo, PageInfo)
        self.totalCount = totalCount
    
    
    def __str__(self):
        return str(self.__dict__)
