from oauthlib.oauth2 import TokenExpiredError

from src.utils import *


class BaseEntity:
    client = None

    def __init__(self, onsign):
        self.client = onsign.get_session()
        self.url = onsign.get_base_url()
    
    def post(self, query_json, _returntype):
        try:
            response = self.client.post(self.url, json=query_json)
            response = self._process_response(response)["data"][_returntype.__name__.lower()]
            print(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.post(data)
        
        return from_json(response, _returntype)

    def _raise_exception(self, response):
        json_data = response.json()
        if 'error' in json_data:
            code = str(json_data['error']['code'])
            raise Exception('OmmaSign error ' + code + ' occured: ' + json_data['error']['message'])
        else:
            response.raise_for_status()
            
    def _process_response(self, response):
        if (response.status_code in [200, 201]):
            self.lastFailed = False
            return response.json()
        else:
            self._raise_exception(response)