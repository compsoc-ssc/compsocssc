from django.contrib import admin
from general import models

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    fields=['fb_id','name','alumni','role']
    list_display=['name','fb_id']
    list_filter=['alumni']
class TrackAdmin(admin.ModelAdmin):
    list_display=['ip','url','agent','time']
    list_filter=['url','agent','time']
    search_fields=['ip']
admin.site.register(models.CompMember,MemberAdmin)
admin.site.register(models.Variable)
admin.site.register(models.Track,TrackAdmin)
