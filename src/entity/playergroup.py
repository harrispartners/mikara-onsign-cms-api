from src.entity.playerloop import PlayerLoop
from src.utils import *


class PlayerGroup:
    id = None
    name = None
    tags = None
    loop = None
    players = None
    
    
    def __init__(self,
                 id,
                 name=None,
                 tags=None,
                 loop=None,
                 players=None):
        self.id = id
        self.name = name
        self.tags = from_json_list(tags, str)
        self.loop = from_json(loop, PlayerLoop)
        from src.entity.playerconnection import PlayerConnection
        self.players = from_json(players, PlayerConnection)
    
    
    def __str__(self):
        return str(self.__dict__)
    
    
    @staticmethod
    def parse(json_data):
        if type(json_data) is str:
            json_data = json.loads(json_data)   # Create into a json dict if it's not
        
        json_data = json_data['data']['organization']['playerGroup']
        
        return PlayerGroup(**json_data)