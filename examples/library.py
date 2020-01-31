from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting libraries...')
    print('[GET] /library endpoint.')
    result = factory.get_entity('Library').get(data={
        # 'mediaId': 9,
        # 'media': 'Aileron Regular',
        # 'type': 'font',
        # 'ownerId': 1,
        # 'retired': 0,
        # 'tags': '',
        # 'exactTags': 0,
        # 'duration': '',
        # 'fileSize': '',
        # 'ownerUserGroupId': 0,
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding media...')
#     print('[POST] /library endpoint.')
#     result = factory.get_entity('Library').post(data={
#         'files': '',
#         'name': 'Test Media File.',
#         'oldMediaId': 0,
#         'updateInLayouts': 0,
#         'deleteOldRevisions': 0,
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing media...')
#     print('[PUT] /library/{mediaId} endpoint.')
#     result = factory.get_entity('Library').put(
#         id=23,
#         data={
#             'name': 'Test Media File Modified',
#             'duration': 5,
#             'retired': 1,
#             'tags': '',
#             'updateInLayouts': 0,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting media...')
#     print('[DELETE] /library/{mediaId} endpoint.')
#     result = factory.get_entity('Library').delete(
#         id=23,
#         data={
#             'forceDelete': 1,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Executing tidy routine...')
#     print('[DELETE] /library/tidy endpoint.')
#     result = factory.get_entity('Library').tidy(
#         data={
#             'tidyGenericFiles': 0,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Downloading media file...')
#     print('[GET] /library/download/{mediaId}/{type} endpoint.')
#     result = factory.get_entity('Library').download(id=22, type='image')
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Tagging media file...')
#     print('[POST] /library/{mediaId}/tag endpoint.')
#     result = factory.get_entity('Library').tag(
#         id=22,
#         data={
#             'tag': ['test media tag'],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting media file tag...')
#     print('[DELETE] /library/{mediaId}/untag endpoint.')
#     result = factory.get_entity('Library').untag(
#         id=22,
#         data={
#             'tag': ['test media tag'],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Getting library item usage report...')
#     print('[GET] /library/usage/{mediaId} endpoint.')
#     result = factory.get_entity('Library').usage(id=22)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Getting library item usage report for layouts...')
#     print('[GET] /library/usage/layouts/{mediaId} endpoint.')
#     result = factory.get_entity('Library').usage_layouts(id=22)
#     print(result)
# except Exception as e:
#     print(e)
