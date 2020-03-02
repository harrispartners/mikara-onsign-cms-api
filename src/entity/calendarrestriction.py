from src.utils import *


class CalendarRestriction:
    weekDays = None
    startTime = None
    endTime = None
    startDate = None
    endDate = None
    isEndStrict = None


    def __init__(self,
                 weekDays=None,
                 startTime=None,
                 endTime=None,
                 startDate=None,
                 endDate=None,
                 isEndStrict=None):
        self.weekDays = from_json_list(weekDays, int)
        self.startTime = parseTimeString(startTime)
        self.endTime = parseTimeString(endTime)
        self.startDate = parseDateTimeString(startDate)
        self.endDate = parseDateTimeString(endDate)
        self.isEndStrict = isEndStrict
    
    
    def __str__(self):
        return str(self.__dict__)