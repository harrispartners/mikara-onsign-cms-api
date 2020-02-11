import graphene

from src.entity.report import Report
from src.entity.contentconnection import ContentConnection
from src.types import *


class RecurringMediaReport(Report):
    showOnlyViewerInteractions = graphene.Boolean(required=True)
    includePartialPlayback = graphene.Boolean(required=True)
    media = graphene.Field(ContentConnection)
    name = graphene.String(required=True)
    schedule = graphene.String(required=True)
    periodAmount = graphene.Int(required=True)
    periodType = graphene.Field(ReportPeriodType, required=True)
    periodOffsetDays = graphene.Int(required=True)
    nextRecurrence = graphene.types.datetime.Date()
    savedReports = graphene.Field(ContentConnection)
    
    
    def __init__(self):
        super(RecurringMediaReport, self).__init__()
