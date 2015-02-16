from django.contrib import admin
from general import models

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    fields=['fb_id','name','alumni','role']
    list_display=['name','fb_id']
    list_filter=['alumni']
admin.site.register(models.CompMember,MemberAdmin)
admin.site.register(models.Variable)
