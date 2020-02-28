from src.onsign import OnSign
from src.entity.base_entity import BaseEntity
from src.entity.organization import Organization
from src.entity.player import Player
from src.entity.playerconnection import PlayerConnection
from src.entity.playergroup import PlayerGroup
from src.entity.playergroupconnection import PlayerGroupConnection
from src.entity.playlist import Playlist
from src.entity.playlistconnection import PlaylistConnection
from src.entity.campaign import Campaign
from src.entity.campaignconnection import CampaignConnection
from src.entity.content import Content
from src.entity.contentconnection import ContentConnection
from src.entity.report import Report
from src.entity.reportconnection import ReportConnection


class OnSignFactory:
    ENTITIES = {
        'Organization': Organization,
        'Player': Player,
        'PlayerConnection': PlayerConnection,
        'PlayerGroup': PlayerGroup,
        'PlayerGroupConnection': PlayerGroupConnection,
        'Playlist': Playlist,
        'PlaylistConnection': PlaylistConnection,
        'Campaign': Campaign,
        'CampaignConnection': CampaignConnection,
        'Content': Content,
        'ContentConnection': ContentConnection,
        'Report': Report,
        'ReportConnection': ReportConnection
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
