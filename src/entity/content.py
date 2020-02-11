import graphene

from src.entity.playable import Playable
from src.entity.contentconnection import ContentConnection
from types import *


class Content(Playable):
    kind = graphene.Field(graphene.NonNull(ContentKind))
    lastModified = graphene.types.datetime.DateTime(required=True)
    size = graphene.Int()
    parentId = graphene.ID()
    ancestorIds = graphene.List(graphene.NonNull(graphene.ID), required=True)
    downloadURL = graphene.String()
    children = graphene.Field(ContentConnection)
    

    def __init__(self):
        super(Content, self).__init__()