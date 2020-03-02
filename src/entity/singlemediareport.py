from src.entity.report import Report
from src.utils import *


class SingleMediaReport(Report):
    showOnlyViewerInteractions = None
    includePartialPlayback = None
    media = None
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
                 showOnlyViewerInteractions=None,
                 includePartialPlayback=None,
                 media=None,
                 periodStart=None,
                 periodEnd=None,
                 savedReport=None):
        super(SingleMediaReport, self).__init__(id,
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
        self.periodStart = parseDateTimeString(periodStart)
        self.periodEnd = parseDateTimeString(periodEnd)
        from src.entity.content import Content
        self.savedReport = from_json(savedReport, Content)
    
    
    def __str__(self):
        return str(self.__dict__)