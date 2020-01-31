from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from src.entity.base_entity import BaseEntity


class Display(BaseEntity):
    def __init__(self, xibo):
        super(Display, self).__init__(xibo, '/display')

    def request_screenshot(self, id=0, data={}):
        try:
            url = self.url + '/requestscreenshot/' + str(id)
            response = self.client.put(url, data=data)
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.request_screenshot(id, data)
        
        return response
        

    def wol(self, id=0, data={}):
        self.url = self.url + '/wol/' + str(id)
        return self.post(data=data)
