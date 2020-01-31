from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting templates...')
    print('[GET] /template endpoint.')
    result = factory.get_entity('Template').get(data={})
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding template from layout...')
#     print('[POST] /template/{layoutId} endpoint.')
#     result = factory.get_entity('Template').add(
#         id=1,
#         data={
#             'includeWidgets': 1,
#             'name': 'Template Test',
#             'tags': '',
#             'description': 'Template Test Description',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)
