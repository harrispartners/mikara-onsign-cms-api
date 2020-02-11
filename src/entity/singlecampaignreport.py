import graphene

from src.entity.report import Report
from src.entity.campaignconnection import CampaignConnection
from src.entity.content import Content
from src.types import *


class SingleCampaignReport(Report):
    includePartialPlayback = graphene.Boolean(required=True)
    campaignTags = graphene.List(graphene.NonNull(graphene.String))
    campaigns = graphene.Field(CampaignConnection)
    periodStart = graphene.types.datetime.DateTime(required=True)
    periodEnd = graphene.types.datetime.DateTime(required=True)
    savedReport = graphene.Field(Content)
    
    
    def __init__(self):
        super(SingleCampaignReport, self).__init__()
