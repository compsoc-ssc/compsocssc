from django.contrib import admin
from orfik import models
class AidAdmin(admin.TabularInline):
    model=models.Aid
class QuestionAdmin(admin.ModelAdmin):
    inlines=[AidAdmin]
    list_display=['number','__str__']
admin.site.register(models.Player)
admin.site.register(models.Question,QuestionAdmin)
# Register your models here.
