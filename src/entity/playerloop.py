from src.entity.playable import Playable
from src.types import *


class PlayerLoop:
    id = None
    kind = None
    items = None
    
    
    def __init__(self, id, kind, items, _subtype):
        self.id = id
        self.kind = kind
        #self.items = [_subtype(x) for x in items]