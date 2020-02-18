import graphene

from src.entity.playable import Playable
from src.entity.restriction import Restriction


class Campaign(Playable):
    category = None
    tags = None
    isPaused = None
    restrictions = None


    def __init__(self, id, name, category, tags, isPaused, restrictions):
        super(Campaign, self).__init__(id, name)
        
        self.category = category
        self.tags = tags
        self.isPaused = isPaused
        self.restrictions = restrictions