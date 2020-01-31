from src.entity.base_entity import BaseEntity


class DisplayProfile(BaseEntity):
    def __init__(self, xibo):
        super(DisplayProfile, self).__init__(xibo, '/displayprofile')
