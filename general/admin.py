from django.contrib import admin
from general import models

from django.contrib.auth.models import Group


class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'fb_id']
    list_filter = ['alumni']

admin.site.register(models.CompMember, MemberAdmin)
admin.site.register(models.Variable)

admin.site.unregister(Group)