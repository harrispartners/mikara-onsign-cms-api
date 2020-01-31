from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from src.entity.base_entity import BaseEntity


class Layout(BaseEntity):
    def __init__(self, xibo):
        super(Layout, self).__init__(xibo, '/layout')

    def retire(self, id=0, data={}):
        self.url = self.url + '/retire'
        return self.put(id=id, data=data)

    def copy(self, id=0, data={}):
        self.url = self.url + '/copy/' + str(id)
        return self.post(data=data)

    def tag(self, id=0, data={}):
        self.url = self.url + '/' + str(id) + '/tag'
        return self.post(data=data)

    def untag(self, id=0, data={}):
        try:
            url = self.url + '/' + str(id) + '/untag'
            response = self.client.delete(url, data=data)
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.untag(id, data)
        
        return response

    def status(self, id=0, data={}):
        self.url = self.url + '/status/' + str(id)
        return self.get(data=data)
    
    def search(self, name):
        try:
            response = self.client.get(self.url, params=self._url_encode({ 'layout': name }))
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.search(name)
        
        return response

