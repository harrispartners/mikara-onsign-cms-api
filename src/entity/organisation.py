import graphene

from src.entity.base_entity import BaseEntity
from src.entity.player import Player
from src.entity.playerconnection import PlayerConnection
from src.entity.playergroup import PlayerGroup
from src.entity.playergroups import PlayerGroupConnection
from src.entity.playlist import Playlist
from src.entity.playlistconnection import PlaylistConnection
from src.entity.campaign import Campaign
from src.entity.campaignconnection import CampaignConnection
from src.entity.content import Content
from src.entity.contentconnection import ContentConnection
from src.entity.report import Report
from src.entity.reportconnection import ReportConnection
from src.types import *


class Organization(BaseEntity):
    id = graphene.ID(required=True)
    name = graphene.String()
    player = graphene.Field(Player)
    players = graphene.Field(PlayerConnection)
    playerGroup = graphene.Field(PlayerGroup)
    playerGroups = graphene.Field(PlayerGroups)
    playlist = graphene.Field(Playlist)
    playlists = graphene.Field(PlaylistConnection)
    campaign = graphene.Field(Campaign)
    campaigns = graphene.Field(CampaignConnection)
    contentRoot = graphene.Field(Content, required=True)
    content = graphene.Field(Content)
    contents = graphene.Field(ContentConnection)
    report = graphene.Field(Report)
    reports = graphene.Field(ReportConnection)
    
    
    def __init__(self):
        super(Organization, self).__init__()