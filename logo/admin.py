from django.contrib import admin
from logo.models import Submission

class SubmissionAdmin(admin.ModelAdmin):
    list_display=['thumbnail','tagline','name','college_name']
    search_fields=['name','college_name','tagline','email']
admin.site.register(Submission, SubmissionAdmin)
