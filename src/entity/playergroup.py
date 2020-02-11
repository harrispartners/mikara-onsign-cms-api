import graphene

from src.entity.base_entity import BaseEntity
from src.entity.playerloop import PlayerLoop
from src.entity.playerconnection import PlayerConnection


class PlayerGroup(BaseEntity):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    tags = graphene.List(graphene.NonNull(graphene.String), required=True)
    loop = graphene.Field(PlayerLoop)
    players = graphene.Field(PlayerConnection)
    
    
    def __init__(self):
        super(PlayerGroup, self).__init__()
