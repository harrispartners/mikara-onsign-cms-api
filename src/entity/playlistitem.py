from src.entity.restriction import Restriction
from src.entity.playable import Playable
from src.utils import *


class PlaylistItem:
    id = None
    position = None
    restrictions = None
    isPaused = None
    node = None
    
    
    def __init__(self,
                 id,
                 position=None,
                 restrictions=None,
                 isPaused=None,
                 node=None):
        self.id = id
        self.position = position
        self.restrictions = from_json(restrictions, Restriction)
        self.isPaused = isPaused
        self.node = node
    
    
    def __str__(self):
        return str(self.__dict__)