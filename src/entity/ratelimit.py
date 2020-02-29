import json


class RateLimit:
    nodeCount = None
    maxNodeCount = None
    cost = None
    limit = None
    remaining = None
    retryAfter = None
    resetAt = None
    
    
    def __init__(self,
                 nodeCount=None,
                 maxNodeCount=None,
                 cost=None,
                 limit=None,
                 remaining=None,
                 retryAfter=None,
                 resetAt=None):
        self.nodeCount = nodeCount
        self.maxNodeCount = maxNodeCount
        self.cost = cost
        self.limit = limit
        self.remaining = remaining
        self.retryAfter = retryAfter
        self.resetAt = resetAt
        
        
    def __str__(self):
        return str(self.__dict__)
    
    
    @staticmethod
    def parse(json_data):
        if json_data is None:
            return None
        
        if type(json_data) is str:
            json_data = json.loads(json_data)   # Create into a json dict if it's not
        
        json_data = json_data['data']['rateLimit']
        
        return RateLimit(**json_data)