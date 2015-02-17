from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Submission(models.Model):
    name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='logo_submissions')
    tagline = models.CharField(max_length=100)
    def __str__(self):return self.name
    def thumbnail(self):
        if self.logo:
            addr=self.logo.url
            addr.strip('/')
            return u'<img src="'+addr+'" width=60 height=60 />'
        else:
            return u'No image file found'
    thumbnail.short_description ='Thumbnail'
    thumbnail.allow_tags=True
        
