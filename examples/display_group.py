from config_load import ConfigLoad

config = ConfigLoad()

from src.xibo_factory import XiboFactory


factory = XiboFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_ID': config.get('CLIENT_ID'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})

try:
    print('Getting display groups...')
    print('[GET] /displaygroup endpoint.')
    result = factory.get_entity('DisplayGroup').get(data={
        # 'displayGroupId': 2,
        # 'displayGroup': 'Test Group2',
        # 'displayId': 1,
        # 'nestedDisplayId': 1,
        # 'dynamicCriteria': '',
    })
    print(result)
except Exception as e:
    print(e)

# try:
#     print('Adding display group...')
#     print('[POST] /displaygroup endpoint.')
#     result = factory.get_entity('DisplayGroup').post(data={
#         'displayGroup': 'Test Group',
#         'description': 'This a Test Group',
#         'isDynamic': 0,
#         'dynamicCriteria': '',
#     })
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Editing display group...')
#     print('[PUT] /displaygroup/{displayGroupId} endpoint.')
#     result = factory.get_entity('DisplayGroup').put(
#         id=2,
#         data={
#             'displayGroup': 'Test Group Modified',
#             'description': 'This a Test Group with a modification',
#             'isDynamic': 0,
#             'dynamicCriteria': '',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Deleting display group...')
#     print('[DELETE] /displaygroup/{displayGroupId} endpoint.')
#     result = factory.get_entity('DisplayGroup').delete(id=2)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Assigning displays to display group...')
#     print('[POST] /displaygroup/{displayGroupId}/display/assign endpoint.')
#     result = factory.get_entity('DisplayGroup').display_assign(
#         id=2,
#         data={
#             'displayId[]': [1],
#             # 'unassignDisplayId[]': [1],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Unassigning displays from display group...')
#     print('[POST] /displaygroup/{displayGroupId}/display/unassign endpoint.')
#     result = factory.get_entity('DisplayGroup').display_unassign(
#         id=2,
#         data={
#             'displayId[]': [1, 2],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Assigning display groups to another display group...')
#     print('[POST] /displaygroup/{displayGroupId}/displayGroup/assign endpoint.')
#     result = factory.get_entity('DisplayGroup').display_group_assign(
#         id=2,
#         data={
#             'displayGroupId': [3, 4],
#             # 'unassignDisplayGroupId': [3, 4],
#         }
#     )
#     print(result)
# except Exception as e:
#      print(e)

# try:
#     print('Unassigning displays from display group...')
#     print('[POST] /displaygroup/{displayGroupId}/displayGroup/unassign endpoint.')
#     result = factory.get_entity('DisplayGroup').display_group_unassign(
#         id=2,
#         data={
#             'displayGroupId': [3, 4],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Assigning media to display group...')
#     print('[POST] /displaygroup/{displayGroupId}/media/assign endpoint.')
#     result = factory.get_entity('DisplayGroup').media_assign(
#         id=2,
#         data={
#             'mediaId': [1, 2],
#             # 'unassignMediaId': [2],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Unassigning media from display group...')
#     print('[POST] /displaygroup/{displayGroupId}/media/unassign endpoint.')
#     result = factory.get_entity('DisplayGroup').media_unassign(
#         id=2,
#         data={
#             'mediaId': [1, 2],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Assigning layout to display group...')
#     print('[POST] /displaygroup/{displayGroupId}/layout/assign endpoint.')
#     result = factory.get_entity('DisplayGroup').layout_assign(
#         id=2,
#         data={
#             'layoutId': [1, 2],
#             # 'unassignLayoutId': [2],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Unassigning layout from display group...')
#     print('[POST] /displaygroup/{displayGroupId}/layout/unassign endpoint.')
#     result = factory.get_entity('DisplayGroup').layout_unassign(
#         id=2,
#         data={
#             'layoutId': [1, 2],
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Setting version instructions to display group...')
#     print('[POST] /displaygroup/{displayGroupId}/version endpoint.')
#     result = factory.get_entity('DisplayGroup').version(
#         id=2,
#         data={
#             'mediaId': 1,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Sending collect now action to display group...')
#     print('[POST] /displaygroup/{displayGroupId}/action/collectNow endpoint.')
#     result = factory.get_entity('DisplayGroup').collect_now(id=2)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Clearing stats and logs in the display group...')
#     print('[POST] /displaygroup/{displayGroupId}/action/clearStatsAndLogs endpoint.')
#     result = factory.get_entity('DisplayGroup').clear_stats_and_logs(id=2)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Sending the change layout action to the display group...')
#     print('[POST] /displaygroup/{displayGroupId}/action/changeLayout endpoint.')
#     result = factory.get_entity('DisplayGroup').change_layout(
#         id=2,
#         data={
#             'layoutId': 1,
#             'duration': 5,
#             'downloadRequired': 0,
#             'changeMode': '',
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Sending the revert to schedule action to display group...')
#     print('[POST] /displaygroup/{displayGroupId}/action/revertToSchedule endpoint.')
#     result = factory.get_entity('DisplayGroup').revert_to_schedule(id=2)
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Sending the the overlay layout action to the display group...')
#     print('[POST] /displaygroup/{displayGroupId}/action/overlayLayout endpoint.')
#     result = factory.get_entity('DisplayGroup').overlay_layout(
#         id=2,
#         data={
#             'layoutId': 1,
#             'duration': 5,
#             'downloadRequired': 0,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)

# try:
#     print('Sending a predefined command to display group...')
#     print('[POST] /displaygroup/{displayGroupId}/action/command endpoint.')
#     result = factory.get_entity('DisplayGroup').command(
#         id=2,
#         data={
#             'commandId': 1,
#         }
#     )
#     print(result)
# except Exception as e:
#     print(e)
