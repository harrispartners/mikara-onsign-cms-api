from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting user displays...')
    print('[GET] /display endpoint.')
    result = factory.get_entity('Display').get(data={
        # 'displayId': 2,
        # 'displayGroupId': '',
        # 'display': 'Android',
        # 'macAddress': '',
        # 'hardwareKey': '',
        # 'clientVersion': '',
        # 'embed': '',
        # 'authorised': 1,
        # 'displayProfileId': 1,
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Editing display...')
#     print('[PUT] /display/{displayId} endpoint.')
#     result = factory.get_entity('Display').put(
#         id=2,
#         data={
#             'display': 'Android Test',
#             'description': 'Test description',
#             'tags': '',
#             'auditingUntil': '',
#             'defaultLayoutId': 8,
#             'licensed': 1,
#             'license': '2f204714-8299-3e28-ab82-c0ad8746ed5c',
#             'incSchedule': 0,
#             'emailAlert': 0,
#             'alertTimeout': 0,
#             'wakeOnLanEnabled': 0,
#             'wakeOnLanTime': '',
#             'broadCastAddress': '',
#             'secureOn': '',
#             'cidr': 0,
#             'latitude': -12,
#             'longitude': 12,
#             'timeZone': 'Australia/Sydney',
#             'displayProfileId': 2,
#             'clearCachedData': 0,
#             'rekeyXmr': 0,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting display...')
#     print('[DELETE] /display/{displayId} endpoint.')
#     result = factory.get_entity('Display').delete(id=2)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Requesting display screenshot...')
#     print('[PUT] /display/requestscreenshot/{displayId} endpoint.')
#     result = factory.get_entity('Display').request_screenshot(id=2)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Sending a wake on LAN packet to the display...')
#     print('[POST] /display/wol/{displayId} endpoint.')
#     result = factory.get_entity('Display').wol(id=2)
#     print(result)
# except Exception as e:
#     print(e)
