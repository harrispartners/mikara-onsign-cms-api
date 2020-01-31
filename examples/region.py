import json

from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

# try:
#     print('Editing layout region...')
#     print('[PUT] /region/{id} endpoint.')
#     result = factory.get_entity('Region').put(
#         id=19,
#         data={
#             'width': 800,
#             'height': 600,
#             'top': 0,
#             'left': 0,
#             'zIndex': 1,
#             'transitionType': '',
#             'transitionDuration': 3600,
#             'transitionDirection': 0,
#             'loop': 0,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting layout region...')
#     print('[DELETE] /region/{regionId} endpoint.')
#     result = factory.get_entity('Region').delete(id=21)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Adding layout region...')
#     print('[POST] /region/{id} endpoint.')
#     result = factory.get_entity('Region').add(
#         id=13,
#         data={
#             'width': 1024,
#             'height': 1024,
#             'top': 50,
#             'left': 50,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Positioning all regions for a layout...')
#     print('[PUT] /region/position/all/{layoutId} endpoint.')
#     result = factory.get_entity('Region').position_all(
#         id=13,
#         data={
#             'regions': [
#                 {
#                     'regionId': 19,
#                     'top': 100,
#                     'left': 100,
#                     'width': 500,
#                     'height': 500,
#                 },
#             ]
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)
