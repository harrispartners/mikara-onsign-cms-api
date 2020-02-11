import graphene

from src.entity.base_entity import BaseEntity
from src.entity.playlist import Playlist
from src.entity.pageinfo import PageInfo
from src.types import *


class PlaylistConnection(BaseEntity):
    nodes = graphene.List(graphene.NonNull(graphene.Field(Playlist)))
    pageInfo = graphene.Field(PageInfo, required=True)
    totalCount = graphene.Int(required=True)
    
    
    def __init__(self):
        super(PlaylistConnection, self).__init__()
