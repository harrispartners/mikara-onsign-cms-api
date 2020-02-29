from src.utils import *


class TagRestriction:
    tags = None
    action = None


    def __init__(self,
                 tags,
                 action):
        self.tags = from_json_list(tags, str)
        self.action = from_json(action, str)
    
    
    def __str__(self):
        return str(self.__dict__)