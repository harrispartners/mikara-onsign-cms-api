

class Playable:
    id = None
    name = None
    
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    
    def __str__(self):
        return str(self.__dict__)