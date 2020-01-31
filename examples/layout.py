from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting layouts...')
    print('[GET] /layout endpoint.')
    result = factory.get_entity('Layout').get(data={
        # 'layoutId': 1,
        # 'layout': 'Default Layout',
        # 'userId': 1,
        # 'retired': 0,
        # 'tags': '',
        # 'exactTags': 0,
        # 'ownerUserGroupId': 0,
        # 'embed': '',
        # '': '',
        # '': '',
        # '': '',
        # '': '',
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding layout...')
#     print('[POST] /layout endpoint.')
#     result = factory.get_entity('Layout').post(data={
#         'name': 'Test Layout',
#         'description': 'Test description layout.',
#         'layoutId': 0,
#         'resolutionId': 9,
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing layout...')
#     print('[PUT] /layout/{layoutId} endpoint.')
#     result = factory.get_entity('Layout').put(
#         id=12,
#         data={
#             'name': 'Test Layout Modified',
#             'description': 'Test description layout modified.',
#             'tags': '',
#             'retired': 1,
#             'backgroundColor': '#FFFFFF',
#             'backgroundImageId': 0,
#             'backgroundzIndex': 0,
#             'resolutionId': 10,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting layout...')
#     print('[DELETE] /layout/{layoutId} endpoint.')
#     result = factory.get_entity('Layout').delete(id=12)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Retiring layout...')
#     print('[PUT] /layout/retire/{layoutId} endpoint.')
#     result = factory.get_entity('Layout').retire(id=13)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Copying layout...')
#     print('[POST] /layout/copy/{layoutId} endpoint.')
#     result = factory.get_entity('Layout').copy(
#         id=13,
#         data={
#             'name': 'Test Layout Copied',
#             'description': 'Test description layout copied.',
#             'copyMediaFiles': 0,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Tagging layout...')
#     print('[POST] /layout/{layoutId}/tag endpoint.')
#     result = factory.get_entity('Layout').tag(
#         id=13,
#         data={
#             'tag': ['test tag'],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting tag...')
#     print('[DELETE] /layout/{layoutId}/untag endpoint.')
#     result = factory.get_entity('Layout').untag(
#         id=13,
#         data={
#             'tag': ['test tag'],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Getting layout status...')
#     print('[GET] /layout/status/{layoutId} endpoint.')
#     result = factory.get_entity('Layout').status(id=13)
#     print(result)
# except Exception as e:
#     print(e)
