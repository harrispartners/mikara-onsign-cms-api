from src.entity.base_entity import BaseEntity


class Notification(BaseEntity):
    def __init__(self, xibo):
        super(Notification, self).__init__(xibo, '/notification')
