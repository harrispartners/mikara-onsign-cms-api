from src.entity.base_entity import BaseEntity


class Statistics(BaseEntity):
    def __init__(self, xibo):
        super(Statistics, self).__init__(xibo, '/stats')
