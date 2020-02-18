import urllib.parse
import requests


class OnSign:
    base_url = ''
    client_secret = ''
    session = None

    def __init__(self, data):
        self.base_url = data['BASE_URL']
        self.client_secret = data['CLIENT_SECRET']

    def get_base_url(self):
        return self.base_url if self.base_url else False

    def get_client_secret(self):
        return self.client_secret if self.client_secret else False

    def get_session(self):
        if self.session is None:
            self.session = requests.Session()
            
            self.session.headers.update({'Authorization': 'token {}'.format(self.client_secret),
                                         'Content-type': 'application/json',
                                         'Accept': 'text/plain'})
        
        return self.session

    def get_cookie(self):
        return self.session.cookies['connect.sid'] if self.session else None
    
    def clear_session(self):
        self.session = None
