from src.entity.report import Report
from src.utils import *


class SingleCampaignReport(Report):
    includePartialPlayback = None
    campaignTags = None
    campaigns = None
    periodStart = None
    periodEnd = None
    savedReport = None
    
    
    def __init__(self,
                 id,
                 contentType=None,
                 periodicity=None,
                 aggregation=None,
                 format=None,
                 notificationEmails=None,
                 playerTags=None,
                 players=None,
                 includePartialPlayback=None,
                 campaignTags=None,
                 campaigns=None,
                 periodStart=None,
                 periodEnd=None,
                 savedReport=None):
        super(SingleCampaignReport, self).__init__(id,
                                                   contentType,
                                                   periodicity,
                                                   aggregation,
                                                   format,
                                                   notificationEmails,
                                                   playerTags,
                                                   players)
        
        self.includePartialPlayback = includePartialPlayback
        self.campaignTags = from_json_list(campaignTags, str)
        from src.entity.campaignconnection import CampaignConnection
        self.campaigns = from_json(campaigns, CampaignConnection)
        self.periodStart = parseDateTimeString(periodStart)
        self.periodEnd = parseDateTimeString(periodEnd)
        from src.entity.content import Content
        self.savedReport = from_json(savedReport, Content)
    
    
    def __str__(self):
        return str(self.__dict__)