from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Submission(models.Model):
    name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    logo = models.ImageField(upload_to=settings.MEDIA_ROOT+'/logo_submissions')
    tagline = models.CharField(max_length=100)


    def __str__(self):
        return ('{} from {}'.format(self.name, self.college_name))
