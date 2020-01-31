from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting time...')
    print('[GET] /clock endpoint.')
    result = factory.get_entity('Clock').get()
    print(result)
except Exception as e:
    print(e)

try:
    print('Getting Xibo CMS about...')
    print('[GET] /about endpoint.')
    result = factory.get_entity('About').get()
    print(result)
except Exception as e:
    print(e)
