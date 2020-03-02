from src.utils import *


class WorkingHours:
    weekDays = None
    startTime = None
    endTime = None
    
    
    def __init__(self,
                 weekDays=None,
                 startTime=None,
                 endTime=None):
        self.weekDays = weekDays
        self.startTime = parseTimeString(startTime)
        self.endTime = parseTimeString(endTime)
    
    
    def __str__(self):
        return str(self.__dict__)