from src.entity.playlists import Playlists
from src.utils import *


class PlayerLoop:
    id = None
    kind = None
    items = None
    
    
    def __init__(self, id, kind, items):
        self.id = id
        self.kind = kind
        self.items = from_json_list(items, Playlists)