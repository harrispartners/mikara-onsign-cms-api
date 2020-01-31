from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting user display profiles...')
    print('[GET] /displayprofile endpoint.')
    result = factory.get_entity('DisplayProfile').get(data={
        # 'displayProfileId': 2,
        # 'displayProfile': 'Windows',
        # 'type': 'android',
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding display profile...')
#     print('[POST] /displayprofile endpoint.')
#     result = factory.get_entity('DisplayProfile').post(data={
#         'name': 'Test Profile',
#         'type': 'android',
#         'isDefault': 0,
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing display profile...')
#     print('[PUT] /displayprofile/{displayProfileId} endpoint.')
#     result = factory.get_entity('DisplayProfile').put(
#         id=6,
#         data={
#             'name': 'Test Profile Modified',
#             'type': 'linux',
#             'isDefault': 1,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting display profile...')
#     print('[DELETE] /displayprofile/{displayProfileId} endpoint.')
#     result = factory.get_entity('DisplayProfile').delete(id=6)
#     print(result)
# except Exception as e:
#     print(e)
