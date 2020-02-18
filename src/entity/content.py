import graphene

from src.entity.playable import Playable
from src.entity.contentconnection import ContentConnection
from types import *


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
        self.lastModified = lastModified
        self.size = size
        self.parentId = parentId
        self.ancestorIds = ancestorIds
        self.downloadURL = downloadURL
        self.children = children