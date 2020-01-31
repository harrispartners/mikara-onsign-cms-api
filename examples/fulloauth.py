# This example is used to show how authenticate and connect
# with the Xibo CMS API in a basic way

from config_load import ConfigLoad
# from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
# from oauthlib.oauth2 import TokenExpiredError


base_api_url = ConfigLoad().get('BASE_URL')
client_id = ConfigLoad().get('CLIENT_ID')
client_secret = ConfigLoad().get('CLIENT_SECRET')

token_url = base_api_url + '/authorize/access_token'
baclient = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=baclient)
token = oauth.fetch_token(
    token_url=token_url,
    client_id=client_id,
    client_secret=client_secret
)

# auth = HTTPBasicAuth(client_id, client_secret)
# baclient = BackendApplicationClient(client_id=client_id)
# oauth = OAuth2Session(client=baclient)
# token = oauth.fetch_token(token_url=token_url, auth=auth)

print(token)

url = base_api_url + '/clock'
client = OAuth2Session(client_id, token=token)
r = client.get(url)
for i in r:
    print(i)
