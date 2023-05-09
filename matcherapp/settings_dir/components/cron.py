# from .settings_dir.components.common import INSTALLED_APPS,MIDDLEWARE
#
# INSTALLED_APPS.append('beatserver')
#
# BEAT_SCHEDULE = {
#     'testing-print': [
#         {
#             # will call test_print method of PrintConsumer
#             'type': 'test.print',
#             # message to pass to the consumer
#             'message': {'testing': 'one'},
#             # Every 5 seconds
#             'schedule': timedelta(seconds=5)
#         },
#         {
#             'type': 'test.print',
#             'message': {'testing': 'two'},
#             # Precisely at 3AM on Monday
#             'schedule': '0 3 * * 1'
#         },
#     ]
# }
