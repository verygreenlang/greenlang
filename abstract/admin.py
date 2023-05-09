from django.contrib import admin


# Register your models here.
class AbstractAdminModel(admin.ModelAdmin):
    readonly_fields = ["id", "history", "last_modification", "created_at"]

    class Meta:
        abstract = True
