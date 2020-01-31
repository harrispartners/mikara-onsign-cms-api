from src.entity.base_entity import BaseEntity


class Template(BaseEntity):
    def __init__(self, xibo):
        super(Template, self).__init__(xibo, '/template')

    def add(self, id=0, data={}):
        self.url = self.url + '/' + str(id)
        return self.post(data=data)
