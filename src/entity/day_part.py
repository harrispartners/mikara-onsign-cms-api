from src.entity.base_entity import BaseEntity


class DayPart(BaseEntity):
    def __init__(self, xibo):
        super(DayPart, self).__init__(xibo, '/daypart')
