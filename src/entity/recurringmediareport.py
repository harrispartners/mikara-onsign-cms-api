from src.entity.report import Report
from src.utils import *


class RecurringMediaReport(Report):
    showOnlyViewerInteractions = None
    includePartialPlayback = None
    media = None
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
                 showOnlyViewerInteractions=None,
                 includePartialPlayback=None,
                 media=None,
                 name=None,
                 schedule=None,
                 periodAmount=None,
                 periodType=None,
                 periodOffsetDays=None,
                 nextRecurrence=None,
                 savedReports=None):
        super(RecurringMediaReport, self).__init__(id,
                                                   contentType,
                                                   periodicity,
                                                   aggregation,
                                                   format,
                                                   notificationEmails,
                                                   playerTags,
                                                   players)
        
        self.showOnlyViewerInteractions = showOnlyViewerInteractions
        self.includePartialPlayback = includePartialPlayback
        from src.entity.contentconnection import ContentConnection
        self.media = from_json(media, ContentConnection)
        self.name = name
        self.schedule = schedule
        self.periodAmount = periodAmount
        self.periodType = periodType
        self.periodOffsetDays = periodOffsetDays
        self.nextRecurrence = nextRecurrence
        self.savedReports = from_json(savedReports, ContentConnection)
    
    
    def __str__(self):
        return str(self.__dict__)