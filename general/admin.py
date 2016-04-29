from django.contrib import admin
from general import models

from image_cropping import ImageCroppingMixin

from django.contrib.auth.models import Group


class MemberAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'batch_of', 'alumni']
    list_filter = ['alumni', 'batch_of']

admin.site.register(models.CompMember, MemberAdmin)
admin.site.register(models.Variable)

admin.site.unregister(Group)