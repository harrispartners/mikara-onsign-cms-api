import graphene

from src.entity.base_entity import BaseEntity
from src.entity.workinghours import WorkingHours
from src.entity.playerloop import PlayerLoop
from src.entity.playergroupconnection import PlayerGroupConnection
from src.types import *


class Player:
    id = None
    name = None
    errorCount = None
    lastSeen = None
    lastSeenAgo = None
    isConnected = None
    syncProgress = None
    signalStrength = None
    timezone = None
    utcOffset = None
    workingHours = None
    version = None
    tags = None
    attrs = None
    updateRequested = None
    updateReady = None
    loop = None
    playerGroups = None
    
    
    def __init__(self,
                 id,
                 name,
                 errorCount,
                 lastSeen,
                 lastSeenAgo,
                 isConnected,
                 syncProgress,
                 signalStrength,
                 timezone,
                 utcOffset,
                 workingHours,
                 version,
                 tags,
                 attrs,
                 updateRequested,
                 updateReady,
                 loop,
                 playerGroups):
        self.id = id
        self.name = name
        self.errorCount = errorCount
        self.lastSeen = lastSeen
        self.lastSeenAgo = lastSeenAgo
        self.isConnected = isConnected
        self.syncProgress = syncProgress
        self.signalStrength = signalStrength
        self.timezone = timezone
        self.utcOffset = utcOffset
        self.workingHours = from_json_list(workingHours, WorkingHours)
        self.version = version
        self.tags = from_json_list(tags, str)
        self.attrs = attrs
        self.updateRequested = updateRequested
        self.updateReady = updateReady
        self.loop = from_jsom(loop, PlayerLoop)
        self.playerGroups = from_json(playerGroups, PlayerGroupConnection)