import json

from src.utils import *


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
                 contentType=None,
                 periodicity=None,
                 aggregation=None,
                 format=None,
                 notificationEmails=None,
                 playerTags=None,
                 players=None):
        self.id = id
        self.contentType = contentType
        self.periodicity = periodicity
        self.aggregation = aggregation
        self.format = format
        self.notificationEmails = from_json_list(notificationEmails, str)
        self.playerTags = from_json_list(playerTags, str)
        from src.entity.playerconnection import PlayerConnection
        self.players = from_json(players, PlayerConnection)
    
    
    def __str__(self):
        return str(self.__dict__)
    
    
    @staticmethod
    def parse(json_data):
        if json_data is None:
            return None
        
        if type(json_data) is str:
            json_data = json.loads(json_data)
        
        json_data = json_data['data']['organization']['report']
        
        if '__typename' in json_data:
            from singlecampaignreport import SingleCampaignReport
            from singlemediareport import SingleMediaReport
            from recurringcampaignreport import RecurringCampaignReport
            from recurringmediareport import RecurringMediaReport
            
            klass = locals()[json_data['__typename']]
        else:
            klass = Report
        
        return klass(**json_data)