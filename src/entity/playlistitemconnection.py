import graphene

from src.entity.base_entity import BaseEntity
from src.entity.playlistitem import PlaylistItem
from src.entity.pageinfo import PageInfo
from src.types import *


class PlaylistItemConnection(BaseEntity):
    edges = graphene.List(graphene.NonNull(graphene.Field(PlaylistItem)))
    pageInfo = graphene.Field(PageInfo, required=True)
    totalCount = graphene.Int(required=True)
    
    
    def __init__(self):
        super(PlaylistItemConnection, self).__init__()
