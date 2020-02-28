from src.entity.playable import Playable
#from src.entity.restriction import Restriction
from src.utils import *


class Playlist(Playable):
    category = None
    tags = None
    isPaused = None
    restrictions = None
    items = None
    
    
    def __init__(self,
                 id,
                 name,
                 category,
                 tags,
                 isPaused,
                 restrictions,
                 items):
        super(Playlist, self).__init__(id, name)
        
        self.category = category
        self.tags = from_json_list(tags, str)
        self.isPaused = isPaused
        #self.restrictions = from_json_list(restrictions, Restriction)
        #self.items = 
    
    
    @staticmethod
    def parse(json_data):
        if json_data is None:
            return None
    
        if type(json_data) is str:
            json_data = json.loads(json_data)   # Create into a json dict if it's not
        
        json_data = json_data['data']['organization']['playlist']
        
        return Playlist(**json_data)