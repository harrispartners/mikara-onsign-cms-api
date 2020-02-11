import graphene

from src.entity.base_entity import BaseEntity


class Playable(graphene.Interface):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    
    
    def __init__(self):
        super(Playable, self).__init__()
