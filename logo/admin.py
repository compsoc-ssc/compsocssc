from django.contrib import admin
from logo.models import Submission

class SubmissionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Submission, SubmissionAdmin)
