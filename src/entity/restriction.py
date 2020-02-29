from src.entity.calendarrestriction import CalendarRestriction
from src.entity.geographicregion import GeographicRegion
from src.entity.tagrestriction import TagRestriction
from src.utils import *


class Restriction:
    calendar = None
    geographic = None
    tag = None
    
    
    def __init__(self,
                 calendar=None,
                 geographic=None,
                 tag=None):
        self.calendar = from_json(calendar, CalendarRestriction)
        self.geographic = from_json_list(geographic, GeographicRegion)
        self.tag = from_json(tag, TagRestriction)
    
    
    def __str__(self):
        return str(self.__dict__)