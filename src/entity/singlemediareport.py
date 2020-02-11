import graphene

from src.entity.report import Report
from src.entity.contentconnection import ContentConnection
from src.entity.content import Content
from src.types import *


class SingleMediaReport(Report):
    showOnlyViewerInteractions = graphene.Boolean(required=True)
    includePartialPlayback = graphene.Boolean(required=True)
    media = graphene.Field(ContentConnection)
    periodStart = graphene.types.datetime.DateTime(required=True)
    periodEnd = graphene.types.datetime.DateTime(required=True)
    savedReport = graphene.Field(Content)
    
    
    def __init__(self):
        super(SingleMediaReport, self).__init__()
