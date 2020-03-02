from src.entity.pageinfo import PageInfo


class ContentConnection:
    nodes = None
    pageInfo = None
    totalCount = None
    
    
    def __init__(self,
                 nodes=None,
                 pageInfo=None,
                 totalCount=None):
        if nodes:
            from src.entity.content import Content
            self.nodes = [Content(**x) for x in nodes]
        
        if pageInfo:
            self.pageInfo = PageInfo(**pageInfo)
        
        if totalCount:
            self.totalCount = totalCount
    
    
    def __str__(self):
        return str(self.__dict__)
    
    
    @staticmethod
    def parse(json_data):
        if json_data is None:
            return None
        
        if type(json_data) is str:
            json_data = json.loads(json_data)
        
        json_data = json_data['data']['organization']['contents']
        
        return ContentConnection(**json_data)