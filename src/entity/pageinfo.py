class PageInfo:
    endCursor = None
    hasNextPage = None
    
    def __init__(self, endCursor, hasNextPage):
        self.endCursor = endCursor
        self.hasNextPage = hasNextPage