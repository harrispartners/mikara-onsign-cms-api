import graphene

from src.entity.base_entity import BaseEntity
'''from src.entity.player import Player
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
from src.entity.reportconnection import ReportConnection'''
from src.types import *
from src.utils import *


class Organization:
    id = None
    name = None
    player = None
    players = None
    playerGroup = None
    playerGroups = None
    playlist = None
    playlists = None
    campaign = None
    campaigns = None
    contentRoot = None
    content = None
    contents = None
    report = None
    reports = None
    
    
    def __init__(self,
                 id,
                 name=None,
                 player=None,
                 players=None,
                 playerGroup=None,
                 playerGroups=None,
                 playlist=None,
                 playlists=None,
                 campaign=None,
                 campaigns=None,
                 contentRoot=None,
                 content=None,
                 contents=None,
                 report=None,
                 reports=None):
        
        self.id = id
        self.name = name
        self.player = from_json(player, Player)
        self.players = from_json(players, PlayerConnection)
        self.playerGroup = from_json(playerGroup, PlayerGroup)
        self.playerGroups = from_json(playerGroups, PlayerGroupConnection)
        self.playlist = from_json(playlist, Playlist)
        self.playlists = from_json(playlists, PlaylistConnection)
        self.campaign = from_json(campaign, Campaign)
        self.campaigns = from_json(campaigns, CampaignConnection)
        self.contentRoot = from_json(contentRoot, Content)
        #if not self.contentRoot:
        #    raise Exception("Required parameter 'contentRoot' was not given.")
        self.content = from_json(content, Content)
        self.contents = from_json(contents, ContentConnection)
        self.report = from_json(report, Report)
        self.reports = from_json(reports, ReportConnection)