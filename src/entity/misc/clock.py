from src.entity.base_entity import BaseEntity


class Clock(BaseEntity):
    def __init__(self, xibo):
        super(Clock, self).__init__(xibo, '/clock')
