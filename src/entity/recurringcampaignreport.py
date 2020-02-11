import graphene

from src.entity.report import Report
from src.entity.campaignconnection import CampaignConnection
from src.entity.contentconnection import ContentConnection
from src.types import *


class RecurringCampaignReport(Report):
    includePartialPlayback = graphene.Boolean(required=True)
    campaignTags = graphene.List(graphene.NonNull(graphene.String))
    campaigns = graphene.Field(CampaignConnection)
    name = graphene.String(required=True)
    schedule = graphene.String(required=True)
    periodAmount = graphene.Int(required=True)
    periodType = graphene.Field(ReportPeriodType, required=True)
    periodOffsetDays = graphene.Int(required=True)
    nextRecurrence = graphene.types.datetime.Date()
    savedReports = graphene.Field(ContentConnection, required=True)
    
    
    def __init__(self):
        super(RecurringCampaignReport, self).__init__()
