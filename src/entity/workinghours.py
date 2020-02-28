from src.utils import *


class WorkingHours:
    weekDays = None
    startTime = None
    endTime = None
    
    
    def __init__(self, weekDays, startTime, endTime):
        self.weekDays = weekDays
        self.startTime = parseTimeString(startTime)
        self.endTime = parseTimeString(endTime)