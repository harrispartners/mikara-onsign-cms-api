import graphene

from src.entity.base_entity import BaseEntity
from src.entity.playergroup import PlayerGroup
from src.entity.pageinfo import PageInfo


class PlayerGroupConnection(BaseEntity):
    nodes = graphene.List(graphene.NonNull(graphene.Field(PlayerGroup)))
    pageInfo = graphene.Field(PageInfo, required=True)
    totalCount = graphene.Int(required=True)
    
    
    def __init__(self):
        super(PlayerGroupConnection, self).__init__()
