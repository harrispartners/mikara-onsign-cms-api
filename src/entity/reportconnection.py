import graphene

from src.entity.base_entity import BaseEntity
from src.entity.report import Report
from src.types import *


class ReportConnection(BaseEntity):
    pageInfo = graphene.Field(PageInfo, required=True)
    nodes = graphene.List(graphene.NonNull(graphene.Field(Report)))
    totalCount = graphene.Int(required=True)
    
    
    def __init__(self):
        super(ReportConnection, self).__init__()
