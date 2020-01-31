from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting statistics...')
    print('[GET] /stats endpoint.')
    result = factory.get_entity('Statistics').get(data={
        # 'type': '',
        # 'fromDt': '',
        # 'toDt': '',
        # 'displayId': 1,
        # 'layoutId': [1],
        # 'mediaId': [1],
    })
    print(result)
except Exception as e:
    print(e)
