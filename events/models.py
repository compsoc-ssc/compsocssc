from django.db import models


class Event(models.Model):
    """
    Description: Model for a CompSoc Event
    """
    name = models.CharField(max_length=120)
    description = models.TextField()
    fb_event_page = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=30)

    PARTICIPATION_METHODS = (
        ('IN', 'Individual'),
        ('TEAMS2', 'Teams of 2'), 
        ('TEAMS2PLUS', 'Teams of 2 or more')
    )
    participation_method = models.CharField(max_length=20,
                                            choices=PARTICIPATION_METHODS,
                                            default=PARTICIPATION_METHODS[0][0])

    def __str__(self):
        return self.name