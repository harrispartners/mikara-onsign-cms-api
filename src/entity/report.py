import graphene

from src.entity.playerconnection import PlayerConnection
from src.types import *


class Report(graphene.Interface):
    id = graphene.ID(required=True)
    contentType = graphene.Field(ReportContentType, required=True)
    periodicity = graphene.Field(ReportPeriodicity, required=True)
    aggregation = graphene.Field(ReportAggregation, required=True)
    format = graphene.Field(ReportFormat, required=True)
    notificationEmails = graphene.List(graphene.NonNull(graphene.String))
    playerTags = graphene.List(graphene.NonNull(graphene.String))
    players = graphene.Field(PlayerConnection)
    
    
    def __init__(self):
        super(Report, self).__init__()