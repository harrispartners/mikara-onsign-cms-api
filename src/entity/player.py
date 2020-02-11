import graphene

from src.entity.base_entity import BaseEntity
from src.entity.workinghours import WorkingHours
from src.entity.playerloop import PlayerLoop
from src.entity.playergroupconnection import PlayerGroupConnection
from src.types import *


class Player(BaseEntity):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    errorCount = graphene.Int(required=True)
    lastSeen = graphene.types.datetime.DateTime()
    lastSeenAgo = graphene.Int()
    isConnected = graphene.Boolean(required=True)
    syncProgress = graphene.Int(required=True)
    signalStrength = graphene.Int()
    timezone = graphene.String()
    utcOffset = graphene.Int()
    workingHours = graphene.List(graphene.NonNull(graphene.Field(WorkingHours)))
    version = graphene.String()
    tags = graphene.List(graphene.NonNull(graphene.String), required=True)
    attrs = graphene.types.json.JSONString()
    updateRequested = graphene.Boolean(required=True)
    updateReady = graphene.String()
    loop = graphene.Field(PlayerLoop)
    playerGroups = graphene.Field(PlayerGroupConnection)
    
    
    def __init__(self):
        super(Player, self).__init__()