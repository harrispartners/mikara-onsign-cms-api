from src.entity.base_entity import BaseEntity


class UserGroup(BaseEntity):
    def __init__(self, xibo):
        super(UserGroup, self).__init__(xibo, '/group')

    def group_copy(self, id=0, data={}):
        self.url = self.url + '/' + str(id) + '/copy'
        return self.post(data=data)
