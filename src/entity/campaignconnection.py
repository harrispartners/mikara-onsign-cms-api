import graphene

from src.entity.base_entity import BaseEntity
from campaign import Campaign
from pageinfo import PageInfo


class CampaignConnection(BaseEntity):
    nodes = graphene.List(graphene.NonNull(graphene.Field(Campaign)))
    pageInfo = graphene.Field(PageInfo, required=True)
    totalCount = graphene.Int(required=True)


    def __init__(self):
        super(CampaignConnection, self).__init__()