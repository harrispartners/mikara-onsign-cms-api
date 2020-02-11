import graphene

from src.entity.base_entity import BaseEntity
from src.entity.player import Player
from src.types import *


class PlayerConnection(BaseEntity):
    pageInfo = graphene.Field(PageInfo, required=True)
    nodes = graphene.List(graphene.NonNull(graphene.Field(Player)))
    totalCount = graphene.Int(required=True)
    
    
    def __init__(self):
        super(PlayerConnection, self).__init__()
