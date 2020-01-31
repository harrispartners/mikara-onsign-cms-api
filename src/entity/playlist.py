from src.entity.base_entity import BaseEntity


class Playlist(BaseEntity):
    def __init__(self, xibo):
        super(Playlist, self).__init__(xibo, '/playlist')

    def widget(self, data={}):
        self.url = self.url + '/widget'
        return self.get(data=data)

    def library_assign(self, id=0, data={}):
        self.url = self.url + '/library/assign/' + str(id)
        return self.post(data=data)
