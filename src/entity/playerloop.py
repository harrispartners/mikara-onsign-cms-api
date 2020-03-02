from src.entity.playlistitemconnection import PlaylistItemConnection
from src.utils import *


class PlayerLoop:
    id = None
    kind = None
    items = None
    
    
    def __init__(self, id, kind=None, items=None):
        self.id = id
        self.kind = kind
        print(items)
        self.items = from_json(items, PlaylistItemConnection)
    
    
    def __str__(self):
        return str(self.__dict__)