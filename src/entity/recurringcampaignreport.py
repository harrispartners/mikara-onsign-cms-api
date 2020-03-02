from src.entity.report import Report
from src.utils import *


class RecurringCampaignReport(Report):
    includePartialPlayback = None
    campaignTags = None
    campaigns = None
    name = None
    schedule = None
    periodAmount = None
    periodType = None
    periodOffsetDays = None
    nextRecurrence = None
    savedReports = None
    
    
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
                 name=None,
                 schedule=None,
                 periodAmount=None,
                 periodType=None,
                 periodOffsetDays=None,
                 nextRecurrence=None,
                 savedReport=None):
        super(RecurringCampaignReport, self).__init__(id,
                                                      contentType,
                                                      periodicity,
                                                      aggregation,
                                                      format,
                                                      notificationEmails,
                                                      playerTags,
                                                      players)
        
        self.includePartialPlayback = includePartialPlayback
        self.campaignTags = campaignTags
        from src.entity.campaignconnection import CampaignConnection
        self.campaigns = from_json(campaigns, CampaignConnection)
        self.name = name
        self.schedule = schedule
        self.periodAmount = periodAmount
        self.periodType = periodType
        self.periodOffsetDays = periodOffsetDays
        self.nextRecurrence = parseDateTimeString(nextRecurrence)
        from src.entity.contentconnection import ContentConnection
        self.savedReport = from_json(savedReport, ContentConnection)
    
    
    def __str__(self):
        return str(self.__dict__)