from src.entity.base_entity import BaseEntity


class DisplayGroup(BaseEntity):
    def __init__(self, xibo):
        super(DisplayGroup, self).__init__(xibo, '/displaygroup')

    def display_assign(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/display/assign'
        return self.post(data=data)

    def display_unassign(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/display/unassign'
        return self.post(data=data)

    def display_group_assign(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/displayGroup/assign'
        return self.post(data=data)

    def display_group_unassign(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/displayGroup/unassign'
        return self.post(data=data)

    def media_assign(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/media/assign'
        return self.post(data=data)

    def media_unassign(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/media/unassign'
        return self.post(data=data)

    def layout_assign(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/layout/assign'
        return self.post(data=data)

    def layout_unassign(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/layout/unassign'
        return self.post(data=data)

    def version(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/version'
        return self.post(data=data)

    def collect_now(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/action/collectNow'
        return self.post(data=data)

    def clear_stats_and_logs(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/action/clearStatsAndLogs'
        return self.post(data=data)

    def change_layout(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/action/changeLayout'
        return self.post(data=data)

    def revert_to_schedule(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/action/revertToSchedule'
        return self.post(data=data)

    def overlay_layout(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/action/overlayLayout'
        return self.post(data=data)

    def command(self, id, data={}):
        self.url = self.url + '/' + str(id) + '/action/command'
        return self.post(data=data)
