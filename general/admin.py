from django.contrib import admin
from general import models


class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'fb_id']
    list_filter = ['alumni']


class TrackAdmin(admin.ModelAdmin):
    list_display = ['ip', 'url', 'agent', 'time']
    list_filter = ['url', 'agent', 'time']
    search_fields = ['ip']


class SiteVisitAdmin(admin.ModelAdmin):
    list_display = ['ip', 'total_access', 'logged_in_access']
    search_fields = ['ip', 'users']

    def total_users(self, obj):
        return obj.users.count()

    total_users.short_description = 'Total users from this ip'
    total_users.allow_tags = True
    
admin.site.register(models.CompMember, MemberAdmin)
admin.site.register(models.SiteVisit, SiteVisitAdmin)
admin.site.register(models.Variable)
# admin.site.register(models.Track,TrackAdmin)
