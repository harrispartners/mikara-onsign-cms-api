from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting campaigns...')
    print('[GET] /campaign endpoint.')
    result = factory.get_entity('Campaign').get(data={
        # 'campaignId': 2,
        'name': 'Test Campaign',
        # 'tags': '',
        # 'hasLayouts': 0,
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding campaign...')
#     print('[POST] /campaign endpoint.')
#     result = factory.get_entity('Campaign').post(data={
#         'name': 'Test Campaign',
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing campaign...')
#     print('[PUT] /campaign/{campaignId} endpoint.')
#     result = factory.get_entity('Campaign').put(
#         id=11,
#         data={
#             'name': 'Test Campaign Modified',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting campaign...')
#     print('[DELETE] /campaign/{campaignId} endpoint.')
#     result = factory.get_entity('Campaign').delete(id=11)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Assgigning layouts to the campaign...')
#     print('[POST] /campaign/layout/assign/{campaignId} endpoint.')
#     result = factory.get_entity('Campaign').layout_assign(
#         id=12,
#         data={
#             'layoutId[0][layoutId]': 8,
#             'layoutId[0][displayOrder]': 1,
#             'layoutId[1][layoutId]': 1,
#             'layoutId[1][displayOrder]': 2,
#             # 'unassignLayoutId[0][layoutId]': 8,
#             # 'unassignLayoutId[0][displayOrder]': 1,
#             # 'unassignLayoutId[1][layoutId]': 1,
#             # 'unassignLayoutId[1][displayOrder]': 2,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)
