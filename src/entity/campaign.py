import graphene

from src.entity.playable import Playable
from src.entity.restriction import Restriction


class Campaign(Playable):
    category = graphene.String(required=True)
    tags = graphene.List(graphene.NonNull(graphene.String), required=True)
    isPaused = graphene.Boolean(required=True)
    restrictions = graphene.List(graphene.NonNull(graphene.Field(Restriction)))


    def __init__(self):
        super(Campaign, self).__init__()