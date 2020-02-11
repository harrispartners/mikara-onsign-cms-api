import graphene

from src.entity.base_entity import BaseEntity
from src.entity.playable import Playable
from src.types import *


class Playlist(Playable):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    category = graphene.String(required=True)
    tags = graphene.List(graphene.NonNull(graphene.String), required=True)
    isPaused = graphene.Boolean(required=True)
    restrictions = graphene.List(graphene.NonNull(graphene.Field(Restriction)))
    items = graphene.List(graphene.Field(Playable))
    
    
    def __init__(self):
        super(Playlist, self).__init__()
