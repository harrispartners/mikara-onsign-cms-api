from src.entity.organization import Organization
'''from src.entity.campaign import Campaign
from src.entity.content import Content'''
from src.entity.playerconnection import PlayerConnection
from src.entity.playergroupconnection import PlayerGroupConnection
from src.onsign import OnSign
from src.entity.base_entity import BaseEntity


class OnSignFactory:
    ENTITIES = {
        'Organization': Organization,
        'PlayerConnection': PlayerConnection,
        'PlayerGroupConnection': PlayerGroupConnection,
        #'Campaign': Campaign,
        #'Content': Content,
    }

    onsign = None

    def __init__(self, config):
        if self.onsign is None:
            self.onsign = OnSign(config)

    def get_entity(self, _type):
        if _type in self.ENTITIES:
            return BaseEntity(self.onsign, self.ENTITIES[_type])
        else:
            raise ValueError('Entity "' + _type + '" doesn\'t exists.')
