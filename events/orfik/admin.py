from django.contrib import admin
from events.orfik import models


def graph(green, total):
    if not total:
        return ('<div style="width: 100px; height: 10px; '
                'border:1px solid black"></div>')
    percentage_passed = int(green * 100.0 / total)
    return ('<div style="width: 100px; height: 10px; border: 1px solid '
            'black; background: red"><div style="width:'
            '' + str(percentage_passed) + 'px; height: 10px; '
            'background: green"></div></div>')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['number', '__str__']


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['nickname','max_level','last_solve','error_rate']
    list_filter = ['max_level']

    def error_rate(self, obj):
        "Returns the error rate of a player"
        attempts = models.Attempt.objects.filter(player=obj).values('correct')
        total = 0.0
        correct = 0.0
        print(attempts)
        for at in attempts:
            total += 1.0
            if at['correct'] == True:
                correct+=1
        return graph(correct, total)

    error_rate.short_description = 'Correct/Wrong attempts'
    error_rate.allow_tags = True

class CredentailsAdmin(admin.ModelAdmin):
    pass



admin.site.register(models.Attempt)
admin.site.register(models.Player,PlayerAdmin)
admin.site.register(models.Question,QuestionAdmin)
admin.site.register(models.CredentialsModel,CredentailsAdmin)
