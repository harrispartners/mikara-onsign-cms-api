import json


class Report:
    id = None
    contentType = None
    periodicity = None
    aggregation = None
    format = None
    notificationEmails = None
    playerTags = None
    players = None
    
    
    def __init__(self,
                 id,
                 contentType,
                 periodicity,
                 aggregation,
                 format,
                 notificationEmails,
                 playerTags,
                 players):
        self.id = id
        self.contentType = contentType
        self.periodicity = periodicity
        self.aggregation = aggregation
        self.format = format
        self.notificationEmails = notificationEmails
        self.playerTags = playerTags
        self.players = players
    
    
    def __str__(self):
        return str(self.__dict__)
    
    
    @staticmethod
    def parse(json_data):
        if json_data is None:
            return None
        
        if type(json_data) is str:
            json_data = json.loads(json_data)
        
        json_data = json_data['data']['organization']['report']
        
        return Report(**json_data)