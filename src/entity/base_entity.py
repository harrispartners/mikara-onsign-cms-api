from oauthlib.oauth2 import TokenExpiredError

from src.utils import *


class BaseEntity:
    client = None

    def __init__(self, onsign, _type):
        self.client = onsign.get_session()
        self.url = onsign.get_base_url()
        self._type = _type
    
    def post(self, query_json):
        try:
            response = self.client.post(self.url, json=query_json)
            response = self._process_response(response)
            response = getattr(self._type, 'parse')(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.post(data)
        
        return from_json(response, self._type)

    def _raise_exception(self, response):
        json_data = response.json()
        print(json_data)
        if 'errors' in json_data:
            if 'message' in json_data['errors'][0]:
                message = str(json_data['errors'][0]['message'])
            else:
                message = json_data['errors'][0]['extensions']['code'] + \
                            ' at ' + \
                            str(json_data['errors'][0]['locations'][0])
            raise Exception('OnSign error occurred: ' + message + '.')
        else:
            response.raise_for_status()
            
    def _process_response(self, response):
        if (response.status_code in [200, 201]):
            self.lastFailed = False
            return response.json()
        else:
            self._raise_exception(response)