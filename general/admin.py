from django.contrib import admin
from general import models

from image_cropping import ImageCroppingMixin

from django.contrib.auth.models import Group


class MemberAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['alumni']

admin.site.register(models.CompMember, MemberAdmin)
admin.site.register(models.Variable)

admin.site.unregister(Group)