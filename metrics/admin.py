from django.contrib import admin
from metrics import models

@admin.register(models.Hit)
class HitAdmin(admin.ModelAdmin):
    list_display = ('ip', 'url', 'stamp', 'ua')
