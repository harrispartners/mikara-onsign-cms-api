from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from src.entity.base_entity import BaseEntity


class Campaign(BaseEntity):
    def __init__(self, xibo):
        super(Campaign, self).__init__(xibo, '/campaign')

    def layout_assign(self, id=0, data={}):
        self.url = self.url + '/layout/assign/' + str(id)
        return self.post(data=data)
    
    def search(self, name):
        try:
            response = self.client.get(self.url, params=self._url_encode({ 'name': name }))
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.search(name)
        
        return response
