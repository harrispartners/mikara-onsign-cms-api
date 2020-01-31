from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

# try:
#     print('Getting my details...')
#     print('[GET] /user/me endpoint.')
#     result = factory.get_entity('User').me()
#     print(result)
# except Exception as e:
#     print(e)

try:
    print('Getting users...')
    print('[GET] /user endpoint.')
    result = factory.get_entity('User').get(data={
        # 'userId': 1,
        # 'userName': 'Test User',
        # 'userTypeId': 1,
        # 'retired': 0,
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding user...')
#     print('[POST] /user endpoint.')
#     result = factory.get_entity('User').post(data={
#         'userName': 'Test User',
#         'email': 'user@test.local',
#         'userTypeId': 1,
#         'homePageId': 29,
#         'libraryQuota': 0,
#         'password': 'somepass',
#         'groupId': 1,
#         'firstName': 'FirstUser',
#         'lastName': 'LastUser',
#         'phone': '0000000000',
#         'ref1': '',
#         'ref2': '',
#         'ref3': '',
#         'ref4': '',
#         'ref5': '',
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Getting user permission by entity and object...')
#     print('[GET] /user/permissions/{entity}/{objectId} endpoint.')
#     result = factory.get_entity('User').get_permissions(
#         entity='page',
#         object_id=8
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Adding user permissions...')
#     print('[POST] /user/permissions/{entity}/{objectId} endpoint.')
#     result = factory.get_entity('User').set_permissions(
#         entity='page',
#         object_id=8,
#         data={
#             'groupIds': [],
#             'ownerId': 0,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Getting user preferences...')
#     print('[GET] /user/pref endpoint.')
#     result = factory.get_entity('User').get_pref(data={
#         # 'preference': '',
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Adding user preferences...')
#     print('[POST] /user/pref endpoint.')
#     result = factory.get_entity('User').set_pref(
#         preference=[
#             {
#                 'userId': 1,
#                 'option': '',
#                 'value": '',
#             }
#         ]
#     )
#     print(result)
# except Exception as e:
#     print(e)
