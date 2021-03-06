import json

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
        self.player = Player(**player) if player else None
        self.players = PlayerConnection(**players) if players else None
        self.playerGroup = PlayerGroup(**playerGroup) if playerGroup else None
        self.playerGroups = PlayerGroupConnection(**playerGroups) if playerGroups else None
        self.playlist = Playlist(**playlist) if playlist else None
        self.playlists = PlaylistConnection(**playlists) if playlists else None
        self.campaign = Campaign(**campaign) if campaign else None
        self.campaigns = CampaignConnection(**campaigns) if campaigns else None
        self.contentRoot = Content(**contentRoot) if contentRoot else None
        self.content = Content(**content) if content else None
        self.contents = ContentConnection(**contents) if contents else None
        self.report = Report(**report) if report else None
        self.reports = ReportConnection(**reports) if reports else None
    
    
    def __str__(self):
        return str(self.__dict__)
        
        
    @staticmethod
    def parse(json_data):
        if type(json_data) is str:
            json_data = json.loads(json_data)   # Create into a json dict if it's not
        
        json_data = json_data['data']['organization']
        
        return Organization(**json_data)