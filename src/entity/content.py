from src.entity.playable import Playable
from src.entity.contentconnection import ContentConnection

from src.utils import *


class Content(Playable):
    kind = None
    lastModified = None
    size = None
    parentId = None
    ancestorIds = None
    downloadURL = None
    children = None
    
    
    def __init__(self,
                 id,
                 name,
                 kind,
                 lastModified,
                 size,
                 parentId,
                 ancestorIds,
                 downloadURL,
                 children):
        super(Content, self).__init__(id, name)
        
        self.kind = kind
        self.lastModified = parseDateTimeString(lastModified)
        self.size = size
        self.parentId = parentId
        self.ancestorIds = from_json_list(ancestorIds, int)
        self.downloadURL = downloadURL
        self.children = from_json(children, ContentConnection)
    
    
    def __str__(self):
        return str(self.__dict__)
    
    
    @staticmethod
    def parse(json_data):
        if json_data is None:
            return None
        
        if type(json_data) is str:
            json_data = json.loads(json_data)
        
        json_data = json_data['data']['organization']['content']
        
        return Content(**json_data)