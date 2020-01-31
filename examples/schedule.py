import datetime
import time

from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

date_from = datetime.date.today()
date_to = datetime.date.today() + datetime.timedelta(days=5)
# try:
#     print('Getting calendar to schedule events...')
#     print('[GET] /schedule/data/events endpoint.')
#     result = factory.get_entity('Schedule').data_events(data={
#         # 'DisplayGroupIds': [1],
#         'from': time.mktime(date_from.timetuple()),
#         'to': time.mktime(date_to.timetuple()),
#     })
#     print(result)
# except Exception as e:
#     print(e)

try:
    print('Getting event list scheduled in a display group...')
    print('[GET] /schedule/:displayGroupId/events endpoint.')
    result = factory.get_entity('Schedule').events(
        display_group_id=8,
        date='2018-01-18 12:00:00'
    )
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding scheduled event to shown in a display group...')
#     print('[POST] /schedule endpoint.')
#     result = factory.get_entity('Schedule').post(data={
#         'eventTypeId': 1,
#         'campaignId': 8,
#         'commandId': 0,
#         'displayOrder': 0,
#         'isPriority': 0,
#         'displayGroupIds': [8, 9],
#         'dayPartId': 0,
#         'syncTimezone': 0,
#         'fromDt': '2018-01-22 12:00:00',
#         'toDt': '2018-01-22 22:00:00',
#         'recurrenceType': '',
#         'recurrenceDetail': 0,
#         'recurrenceRange': '',
#         'recurrenceRepeatsOn': [],
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing scheduled event...')
#     print('[PUT] /schedule/{eventId} endpoint.')
#     result = factory.get_entity('Schedule').put(
#         id=6,
#         data={
#             'eventTypeId': 1,
#             'campaignId': 8,
#             'commandId': 0,
#             'displayOrder': 0,
#             'isPriority': 0,
#             'displayGroupIds[]': [9],
#             'dayPartId': 0,
#             'syncTimezone': 0,
#             'fromDt': '2018-01-23 12:00:00',
#             'toDt': '2018-01-23 22:00:00',
#             'recurrenceType': '',
#             'recurrenceDetail': 0,
#             'recurrenceRange': '',
#             'recurrenceRepeatsOn': [],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting scheduled event...')
#     print('[DELETE] /schedule/{eventId} endpoint.')
#     result = factory.get_entity('Schedule').delete(id=6)
#     print(result)
# except Exception as e:
#     print(e)
