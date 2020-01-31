from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting day part events...')
    print('[GET] /daypart endpoint.')
    result = factory.get_entity('DayPart').get()
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding day part...')
#     print('[POST] /daypart endpoint.')
#     result = factory.get_entity('DayPart').post(data={
#         'name': 'Test Day Part',
#         'description': 'Test day part description',
#         'startTime': '10:00',
#         'endTime': '20:00',
#         'exceptionDays': [],
#         'exceptionStartTimes': [],
#         'exceptionEndTimes': [],
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing day part...')
#     print('[PUT] /daypart/{dayPartId} endpoint.')
#     result = factory.get_entity('DayPart').put(
#         id=1,
#         data={
#             'name': 'Test Day Part Modified',
#             'description': 'Test day part description modified',
#             'startTime': '11:00',
#             'endTime': '18:00',
#             'exceptionDays': [],
#             'exceptionStartTimes': [],
#             'exceptionEndTimes': [],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting day part...')
#     print('[DELETE] /daypart/{dayPartId} endpoint.')
#     result = factory.get_entity('DayPart').delete(id=1)
#     print(result)
# except Exception as e:
#     print(e)
