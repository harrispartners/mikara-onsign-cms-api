from src.entity.workinghours import WorkingHours
from src.entity.playerloop import PlayerLoop
from src.utils import *


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
                 name=None,
                 errorCount=None,
                 lastSeen=None,
                 lastSeenAgo=None,
                 isConnected=None,
                 syncProgress=None,
                 signalStrength=None,
                 timezone=None,
                 utcOffset=None,
                 workingHours=None,
                 version=None,
                 tags=None,
                 attrs=None,
                 updateRequested=None,
                 updateReady=None,
                 loop=None,
                 playerGroups=None):
        self.id = id
        self.name = name
        self.errorCount = errorCount
        self.lastSeen = setAsTimezone(parseDateTimeString(lastSeen), timezone)
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
        self.loop = from_json(loop, PlayerLoop)
        from src.entity.playergroupconnection import PlayerGroupConnection
        self.playerGroups = from_json(playerGroups, PlayerGroupConnection)
    
    
    def __str__(self):
        return str(self.__dict__)
        
        
    @staticmethod
    def parse(json_data):
        if json_data is None:
            return None
    
        if type(json_data) is str:
            json_data = json.loads(json_data)   # Create into a json dict if it's not
        
        json_data = json_data['data']['organization']['player']
        
        return Player(**json_data)