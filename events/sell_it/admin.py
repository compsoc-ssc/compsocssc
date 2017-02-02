from django.contrib import admin
from events.sell_it.models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'college_name']
    search_fields = ['name', 'college_name','email']

admin.site.register(Submission, SubmissionAdmin)
