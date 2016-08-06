from django.contrib import admin
from django.contrib.auth.models import Group
from .models import NewMember


class NewMemberModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'year', 'timestamp']
    list_filter = ['year', 'course']
    search_fields = ['name', 'course']
    class Meta:
        model = NewMember

admin.site.register(NewMember, NewMemberModelAdmin)