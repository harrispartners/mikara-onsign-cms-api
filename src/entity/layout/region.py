from src.entity.base_entity import BaseEntity


class Region(BaseEntity):
    def __init__(self, xibo):
        super(Region, self).__init__(xibo, '/region')

    def add(self, id=0, data={}):
        self.url = self.url + '/' + str(id)
        return self.post(data=data)

    def position_all(self, id=0, data={}):
        self.url = self.url + '/position/all'
        return self.put(id=id, data=data)
