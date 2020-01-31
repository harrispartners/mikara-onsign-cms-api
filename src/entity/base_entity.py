from multidimensional_urlencode import urlencode
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
try:
    from urllib.parse import unquote
except:
    from urllib import unquote


class BaseEntity:
    client = ''
    url = ''
    funcreset_token = None

    def __init__(self, xibo, path):
        self.client = xibo.get_client()
        self.url = xibo.get_base_url() + path
        self.xibo = xibo

    def _url_encode(self, data):
        encoded_data = urlencode(data)
        unquote(encoded_data)
        return encoded_data

    def _raise_exception(self, response):
        json_data = response.json()
        if 'error' in json_data:
            code = str(json_data['error']['code'])
            raise Exception('Xibo error ' + code + ' occured: ' + json_data['error']['message'])
        else:
            response.raise_for_status()

    def _renew_token(self):
        # Token has expired so we need to clear expired one
        # and force creation of a new one
        self.xibo.clear_token()
        self.client = self.xibo.get_client()

    def _process_response(self, response):
        if (response.status_code in [200, 201]):
            self.lastFailed = False
            return response.json()
        elif (response.status_code == 204):
            return response.text
        else:
            self._raise_exception(response)

    def get(self, data={}):
        try:
            response = self.client.get(self.url, params=self._url_encode(data))
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.get(data)
        
        return response

    def post(self, data={}):
        try:
            response = self.client.post(self.url, data=self._url_encode(data))
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.post(data)
        
        return response

    def put(self, id, data={}):
        try:
            url = self.url + '/' + str(id)
            response = self.client.put(url, data=data)
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.put(id, data)
        
        return response

    def delete(self, id, data={}):
        try:
            url = self.url + '/' + str(id)
            response = self.client.delete(url, data=data)
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.delete(id, data)
        
        return response

