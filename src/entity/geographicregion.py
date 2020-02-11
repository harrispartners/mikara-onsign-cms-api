import graphene

from src.entity.base_entity import BaseEntity


class GeographicRegion(BaseEntity):
    id = graphene.ID(required=True)
    
    
    def __init__(self):
        super(GeographicRegion, self).__init__()