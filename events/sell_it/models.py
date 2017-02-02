from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Submission(models.Model):
    name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    design = models.ImageField(upload_to='design_submissions')

    def __str__(self):
        return self.name

    def thumbnail(self):
        if self.design:
            addr = self.design.url
            addr.strip('/')
            return u'<img src="{}" >'.format(addr)
        else:
            return u'No image file found'

    thumbnail.short_description = 'Thumbnail'
    thumbnail.allow_tags = True
