import graphene

from src.entity.base_entity import BaseEntity


class CalendarRestriction(BaseEntity):
    weekDays = graphene.List(graphene.NonNull(graphene.Int))
    startTime = graphene.types.datetime.Time(required=True)
    endTime = graphene.types.datetime.Time(required=True)
    startDate = graphene.types.datetime.Date()
    endDate = graphene.types.datetime.Date()
    isEndStrict = graphene.Boolean(required=True)


    def __init__(self):
        super(CalendarRestriction, self).__init__()