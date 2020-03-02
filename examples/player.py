from config_load import ConfigLoad
config = ConfigLoad()
from src.onsign import OnSign
from src.onsign_factory import OnSignFactory
from src.entity.organization import Organization

from src.utils import *


factory = OnSignFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})




result = factory.get_entity('Player').post(create_graphql_request(query, True))
print(result)