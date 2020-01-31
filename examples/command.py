from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting user commands...')
    print('[GET] /command endpoint.')
    result = factory.get_entity('Command').get(data={
        # 'commandId': 1,
        # 'command': 'Test Command',
        # 'code': 'testcode',
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding command...')
#     print('[POST] /command endpoint.')
#     result = factory.get_entity('Command').post(data={
#         'command': 'Test Command',
#         'description': 'Test command description',
#         'code': 'testcode',
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing command...')
#     print('[PUT] /command/{commandId} endpoint.')
#     result = factory.get_entity('Command').put(
#         id=1,
#         data={
#             'command': 'Test Command Modified',
#             'description': 'Test command description modified',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting command...')
#     print('[DELETE] /command/{commandId} endpoint.')
#     result = factory.get_entity('Command').delete(id=1)
#     print(result)
# except Exception as e:
#     print(e)
