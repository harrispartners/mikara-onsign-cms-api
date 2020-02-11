import graphene

from src.entity.base_entity import BaseEntity
from src.entity.restriction import Restriction
from src.entity.playable import Playable
from src.types import *


class PlaylistItem(BaseEntity):
    id = graphene.ID(required=True)
    position = graphene.Int()
    restrictions = graphene.List(graphene.NonNull(graphene.Field(Restriction)))
    isPaused = graphene.Boolean(required=True)
    node = graphene.Field(Playable, required=True)
    
    
    def __init__(self):
        super(PlaylistItem, self).__init__()
