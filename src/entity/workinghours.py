import graphene

from src.entity.base_entity import BaseEntity


class WorkingHours(BaseEntity):
    weekDays = graphene.List(graphene.NonNull(graphene.Int), required=True)
    startTime = graphene.types.datetime.Time(required=True)
    endTime = graphene.types.datetime.Time(required=True)


    def __init__(self):
        super(WorkingHours, self).__init__()