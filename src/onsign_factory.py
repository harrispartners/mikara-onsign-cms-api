from src.entity.organization import Organization
'''from src.entity.campaign import Campaign
from src.entity.content import Content'''
from src.onsign import OnSign
from src.entity.base_entity import BaseEntity


class OnSignFactory:
    ENTITIES = {
        'Organization': Organization,
        #'Campaign': Campaign,
        #'Content': Content,
    }

    onsign = None

    def __init__(self, config):
        if self.onsign is None:
            self.onsign = OnSign(config)

    def get_entity(self, _type):
        if _type in self.ENTITIES:
            return BaseEntity(self.onsign)
        else:
            raise ValueError('Entity "' + type + '" doesn\'t exists.')