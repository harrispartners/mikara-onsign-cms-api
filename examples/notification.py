from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting user notifications...')
    print('[GET] /notification endpoint.')
    result = factory.get_entity('Notification').get(data={
        # 'notificationId': 2,
        # 'subject': '',
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding notification...')
#     print('[POST] /notification endpoint.')
#     result = factory.get_entity('Notification').post(data={
#         'subject': 'Test Notification',
#         'body': 'Test body notification',
#         'releaseDt': '2018-01-19 22:00:00',
#         'isEmail': 0,
#         'isInterrupt': 0,
#         'displayGroupIds': [8, 9],
#         'userGroupIds': [],
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing notification...')
#     print('[PUT] /notification/{notificationId} endpoint.')
#     result = factory.get_entity('Notification').put(
#         id=1,
#         data={
#             'subject': 'Test Notification Modified',
#             'body': 'Test body notification modified',
#             'releaseDt': '2018-01-20 22:00:00',
#             'isEmail': 1,
#             'isInterrupt': 0,
#             'displayGroupIds': [9],
#             'userGroupIds': [],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting notification...')
#     print('[DELETE] /notification/{notificationId} endpoint.')
#     result = factory.get_entity('Notification').delete(id=1)
#     print(result)
# except Exception as e:
#     print(e)
