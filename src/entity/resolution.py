from src.entity.base_entity import BaseEntity


class Resolution(BaseEntity):
    def __init__(self, xibo):
        super(Resolution, self).__init__(xibo, '/resolution')
