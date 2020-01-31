from src.entity.base_entity import BaseEntity


class Widget(BaseEntity):
    def __init__(self, xibo):
        super(Widget, self).__init__(xibo, '/playlist/widget')
    
    def edit(self, id, data={}):
        return self.put(id=id, data=data)
