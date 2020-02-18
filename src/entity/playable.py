import graphene

from src.entity.base_entity import BaseEntity


class Playable(BaseEntity):
    id = None
    name = None
    
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
