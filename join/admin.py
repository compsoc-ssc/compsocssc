from django.contrib import admin
from django.contrib.auth.models import Group
from .models import NewMember

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class NewMemberResource(resources.ModelResource):
    class Meta:
        model = NewMember
        exclude = ('id', 'timestamp',)


class NewMemberModelAdmin(ImportExportModelAdmin):
    resource_class = NewMemberResource
    list_display = ['name', 'course', 'year', 'timestamp']
    list_filter = ['year', 'course']
    search_fields = ['name', 'course']
    class Meta:
        model = NewMember

admin.site.register(NewMember, NewMemberModelAdmin)