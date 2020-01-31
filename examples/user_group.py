from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting user groups...')
    print('[GET] /group endpoint.')
    result = factory.get_entity('UserGroup').get(data={
        # 'userGroupId': 1,
        # 'userGroup': 'Users',
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Copying an user group...')
#     print('[POST] /group/{userGroupId}/copy endpoint.')
#     result = factory.get_entity('UserGroup').group_copy(
#         id=1,
#         data={
#             'group': 'Users Copy',
#             'copyMembers': 1,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)
