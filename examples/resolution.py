from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting resolutions...')
    print('[GET] /resolution endpoint.')
    result = factory.get_entity('Resolution').get(data={
        # 'resolutionId': 9,
        # 'resolution': '1080p HD Landscape',
        # 'enabled': 1,
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding resolution...')
#     print('[POST] /resolution endpoint.')
#     result = factory.get_entity('Resolution').post(data={
#         'resolution': 'Test Resolution',
#         'width': 600,
#         'height': 400,
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing resolution...')
#     print('[PUT] /resolution/{resolutionId} endpoint.')
#     result = factory.get_entity('Resolution').put(
#         id=17,
#         data={
#             'resolution': 'Test Resolution Modified',
#             'width': 640,
#             'height': 420,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting resolution...')
#     print('[DELETE] /resolution/{resolutionId} endpoint.')
#     result = factory.get_entity('Resolution').delete(id=17)
#     print(result)
# except Exception as e:
#     print(e)
