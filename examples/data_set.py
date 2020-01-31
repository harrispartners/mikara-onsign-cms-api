from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting data sets...')
    print('[GET] /dataset endpoint.')
    result = factory.get_entity('DataSet').get(data={
        # 'dataSetId': 1,
        # 'dataSet': 'Test Data Set',
        # 'code': 'test_data_set',
        # 'embed': '',
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding data set...')
#     print('[POST] /dataset endpoint.')
#     result = factory.get_entity('DataSet').post(data={
#         'dataSet': 'Test Data Set',
#         'description': 'Test data set description.',
#         'code': 'test_data_set',
#         'isRemote': 0,
#         'method': 'GET',
#         'uri': '',
#         'postData': '',
#         'authentication': 'Basic',
#         'username': '',
#         'password': '',
#         'refreshRate': 5,
#         'clearRate': 0,
#         'runsAfter': 0,
#         'dataRoot': '',
#         'summarize': '',
#         'summarizeField': '',
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing data set...')
#     print('[PUT] /dataset/{dataSetId} endpoint.')
#     result = factory.get_entity('DataSet').put(
#         id=1,
#         data={
#             'dataSet': 'Test Data Set Modified',
#             'description': 'Test data set description modified.',
#             'code': 'test_data_set_modified',
#             'isRemote': 1,
#             'method': 'GET',
#             'uri': '',
#             'postData': '',
#             'authentication': '',
#             'username': '',
#             'password': '',
#             'refreshRate': 5,
#             'clearRate': 0,
#             'runsAfter': 0,
#             'dataRoot': '',
#             'summarize': '',
#             'summarizeField': '',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting data set...')
#     print('[DELETE] /dataset/{dataSetId} endpoint.')
#     result = factory.get_entity('DataSet').delete(id=1)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Copying data set...')
#     print('[POST] /dataset/copy/{dataSetId} endpoint.')
#     result = factory.get_entity('DataSet').copy(
#         id=2,
#         data={
#             'dataSet': 'Test Data Set Copied',
#             'description': 'Test data set copied description.',
#             'code': 'test_data_set_copied',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Getting data set columns...')
#     print('[GET] /dataset/{dataSetId}/column endpoint.')
#     result = factory.get_entity('DataSet').get_column(
#         id=2,
#         data={
#             # 'dataSetColumnId': 0,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Adding data set column...')
#     print('[POST] /dataset/{dataSetId}/column endpoint.')
#     result = factory.get_entity('DataSet').add_column(
#         id=2,
#         data={
#             'heading': 'Column Test 1',
#             'listContent': '',
#             'columnOrder': 2,
#             'dataTypeId': 1,
#             'dataSetColumnTypeId': 1,
#             'formula': '',
#             'remoteField': '',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing data set column...')
#     print('[PUT] /dataset/{dataSetId}/column/{dataSetColumnId} endpoint.')
#     result = factory.get_entity('DataSet').edit_column(
#         id=2,
#         column_id=4,
#         data={
#             'heading': 'Column Test 1 Modified',
#             'listContent': '',
#             'columnOrder': 2,
#             'dataTypeId': 1,
#             'dataSetColumnTypeId': 1,
#             'formula': '',
#             'remoteField': '',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting data set column...')
#     print('[DELETE] /dataset/{dataSetId}/column/{dataSetColumnId} endpoint.')
#     result = factory.get_entity('DataSet').delete_column(id=2, column_id=4)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Getting data for data set...')
#     print('[GET] /dataset/data/{dataSetId} endpoint.')
#     result = factory.get_entity('DataSet').get_data(id=2)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Adding data set row...')
#     print('[POST] /dataset/data/{dataSetId} endpoint.')
#     result = factory.get_entity('DataSet').add_row(
#         id=2,
#         data={
#             'dataSetColumnId_2': 'Test value',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing data set row...')
#     print('[PUT] /dataset/data/{dataSetId}/{rowId} endpoint.')
#     result = factory.get_entity('DataSet').edit_row(
#         id=2,
#         row_id=5,
#         data={
#             'dataSetColumnId_2': 'Test value modified',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting data set row...')
#     print('[DELETE] /dataset/data/{dataSetId}/{rowId} endpoint.')
#     result = factory.get_entity('DataSet').delete_row(id=2, row_id=5)
#     print(result)
# except Exception as e:
#     print(e)
