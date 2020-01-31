from src.entity.base_entity import BaseEntity


class Command(BaseEntity):
    def __init__(self, xibo):
        super(Command, self).__init__(xibo, '/command')
