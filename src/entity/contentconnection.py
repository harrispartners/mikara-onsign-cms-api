import graphene

from src.entity.base_entity import BaseEntity
from src.entity.Content import Content
from src.types import *


class ContentConnection(BaseEntity):
    pageInfo = graphene.Field(PageInfo, required=True)
    nodes = graphene.List(graphene.NonNull(Content))
    totalCount = graphene.Int(required=True)
    
    
    def __init__(self):
        super(ContentConnection, self).__init__()