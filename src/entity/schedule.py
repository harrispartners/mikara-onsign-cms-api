from src.entity.base_entity import BaseEntity


class Schedule(BaseEntity):
    def __init__(self, xibo):
        super(Schedule, self).__init__(xibo, '/schedule')

    def data_events(self, data={}):
        self.url = self.url + '/data/events'
        return self.get(data=data)

    def events(self, display_group_id=0, date=''):
        self.url = self.url + '/' + str(display_group_id) + '/events'
        data = {'date': date}
        return self.get(data=data)
