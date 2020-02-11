import graphene

from src.entity.base_entity import BaseEntity
from src.entity.playable import Playable
from src.types import *


class PlayerLoop(BaseEntity):
    id = graphene.ID(required=True)
    kind = graphene.Field(PlayerLoopType, required=True)
    items = graphene.List(graphene.Field(Playable))
    
    
    def __init__(self):
        super(PlayerLoop, self).__init__()
