from src.entity.misc.about import About
from src.entity.campaign import Campaign
from src.entity.command import Command
from src.entity.misc.clock import Clock
from src.entity.data_set import DataSet
from src.entity.day_part import DayPart
from src.entity.display import Display
from src.entity.display_group import DisplayGroup
from src.entity.display_profile import DisplayProfile
from src.entity.layout.layout import Layout
from src.entity.library import Library
from src.entity.notification import Notification
from src.entity.playlist import Playlist
from src.entity.layout.region import Region
from src.entity.resolution import Resolution
from src.entity.schedule import Schedule
from src.entity.statistics import Statistics
from src.entity.template import Template
from src.entity.user import User
from src.entity.user_group import UserGroup
from src.entity.widget.widget import Widget
from src.entity.widget.textwidget import TextWidget
from src.xibo import Xibo


class XiboFactory:
    ENTITIES = {
        'About': About,
        'Campaign': Campaign,
        'Command': Command,
        'Clock': Clock,
        'DataSet': DataSet,
        'DayPart': DayPart,
        'Display': Display,
        'DisplayGroup': DisplayGroup,
        'DisplayProfile': DisplayProfile,
        'Layout': Layout,
        'Library': Library,
        'Notification': Notification,
        'Playlist': Playlist,
        'Region': Region,
        'Resolution': Resolution,
        'Schedule': Schedule,
        'Statistics': Statistics,
        'Template': Template,
        'User': User,
        'UserGroup': UserGroup,
        'Widget': Widget,
        'TextWidget': TextWidget,
    }

    xibo = None

    def __init__(self, config):
        if self.xibo is None:
            self.xibo = Xibo(config)

    def get_entity(self, type):
        if type in self.ENTITIES:
            return self.ENTITIES[type](self.xibo)
        else:
            raise ValueError('Entity "' + type + '" doesn\'t exists.')
