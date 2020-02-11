import graphene

from src.entity.base_entity import BaseEntity
from src.entity.calendarrestriction import CalendarRestriction
from src.entity.geographicregion import GeographicRegion
from src.entity.tagrestriction import TagRestriction
from src.types import *


class Restriction(BaseEntity):
    calendar = graphene.Field(CalendarRestriction)
    geographic = graphene.List(graphene.NonNull(graphene.Field(GeographicRegion)))
    tag = graphene.Field(TagRestriction)
    
    
    def __init__(self):
        super(Restriction, self).__init__()
