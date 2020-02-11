import graphene

from src.entity.base_entity import BaseEntity
from src.types import *


class TagRestriction(BaseEntity):
    tags = graphene.List(graphene.NonNull(graphene.String), required=True)
    action = graphene.Field(TagRestrictionActions, required=True)


    def __init__(self):
        super(TagRestriction, self).__init__()