from src.entity.base_entity import BaseEntity


class About(BaseEntity):
    def __init__(self, xibo):
        super(About, self).__init__(xibo, '/about')
