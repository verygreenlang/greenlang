from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportMixin
from import_export.admin import ImportExportModelAdmin

from django_q import models as q_models
from django_q import admin as q_admin
from django.contrib import admin


#
# from import_export import resources, fields
#
#
# class PersonDetailsAdminResource(resources.ModelResource):
#     class Meta:
#         model = q_models.Schedule
#         fields = (
#             'id',
#             'Name',
#             'Func',
#             'Hook',
#             'Args',
#             'Kwargs',
#             'Schedule_Type',
#             'Minutes',
#             'Repeats',
#             'Next_Run',
#             'Cluster',
#         )



admin.site.unregister([q_models.Schedule])
@admin.register(q_models.Schedule)
class ChildClassAdmin(ImportExportModelAdmin,q_admin.ScheduleAdmin):
    pass
#     pass
    # resource_class = PersonDetailsAdminResource
    # list_display=("Func",)
    # list_display = (
    #     'name',
    #     'func',
    #     'result',
    #     'started',
    #     # add attempt_count to list_display
    #     'attempt_count'
    # )
