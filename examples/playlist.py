from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting widgets from playlist...')
    print('[GET] /playlist/widget endpoint.')
    result = factory.get_entity('Playlist').widget(data={
        'playlistId': 5,
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding media from library to the playlist...')
#     print('[POST] /playlist/library/assign/{playlistId} endpoint.')
#     result = factory.get_entity('Playlist').library_assign(
#         id=5,
#         data={
#             'media': [22],
#             # 'duration[]': 10,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)
