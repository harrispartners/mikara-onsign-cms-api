from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient


class OnSign:
    base_url = ''
    client_id = ''
    client_secret = ''
    token = ''

    def __init__(self, data):
        self.base_url = data['BASE_URL']
        self.client_id = data['CLIENT_ID']
        self.client_secret = data['CLIENT_SECRET']

    def get_base_url(self):
        return self.base_url if self.base_url else False

    def get_client_id(self):
        return self.client_id if self.client_id else False

    def get_client_secret(self):
        return self.client_secret if self.client_secret else False

    def get_token(self):
        if not self.token:
            token_url = self.base_url + '/authorize/access_token'
            client = BackendApplicationClient(client_id=self.client_id)
            oauth = OAuth2Session(client=client)
            self.token = oauth.fetch_token(
                token_url=token_url,
                client_id=self.client_id,
                client_secret=self.client_secret
            )

        return self.token

    def get_client(self):
        return OAuth2Session(self.client_id, token=self.get_token())
    
    def clear_token(self):
        self.token = ''

