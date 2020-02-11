import graphene

from src.entity.base_entity import BaseEntity


class PageInfo(BaseEntity):
    endCursor = graphene.String()
    hasNextPage = graphene.Boolean()
    
    
    def __init__(self):
        super(PageInfo, self).__init__()