from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from src.entity.base_entity import BaseEntity


class Library(BaseEntity):
    def __init__(self, xibo):
        super(Library, self).__init__(xibo, '/library')

    def search(self, media, mediatype):
        try:
            response = self.client.get(self.url, params=self._url_encode({ 'media': media, 'type': mediatype }))
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.search(media, mediatype)
        
        return response

    def tidy(self, data={}):
        try:
            url = self.url + '/tidy'
            response = self.client.delete(url, data=data)
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.tidy(data)
        
        return response

    def upload(self, files):
        return self.client.post(self.url, files=files)

    def download(self, id=0, type='image'):
        self.url = self.url + '/download/' + str(id) + '/' + str(type)
        return self.get()

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

    def usage(self, id=0):
        self.url = self.url + '/usage/' + str(id)
        return self.get()

    def usage_layouts(self, id=0):
        self.url = self.url + '/usage/layouts/' + str(id)
        return self.get()
