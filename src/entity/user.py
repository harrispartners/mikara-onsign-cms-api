from src.entity.base_entity import BaseEntity


class User(BaseEntity):
    def __init__(self, xibo):
        super(User, self).__init__(xibo, '/user')

    def me(self):
        self.url = self.url + '/me'
        return self.get()

    def get_permissions(self, entity='', object_id=0):
        self.url = self.url + '/permissions/' + entity + '/' + str(object_id)
        return self.get()

    def set_permissions(self, entity='', object_id=0, data={}):
        self.url = self.url + '/permissions/' + entity + '/' + str(object_id)
        return self.post(data=data)

    def get_pref(self, data={}):
        self.url = self.url + '/pref'
        return self.get(data=data)

    def set_pref(self, data={}):
        self.url = self.url + '/pref'
        return self.post(data=data)
