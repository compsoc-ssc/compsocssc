from django.db import models
from django.utils import timezone
from django.conf import settings
import requests


USER = settings.AUTH_USER_MODEL

class CompMember(models.Model):
    """A member of compsoc"""

    class Meta:
        verbose_name = 'CompSoc Member'
        verbose_name_plural = 'CompSoc Members'

    fb_id = models.CharField(max_length=20, help_text='Facebook ID:')
    fb_image_url = models.TextField()
    name = models.CharField(max_length=20)
    alumni = models.BooleanField(default=False)
    role = models.CharField(max_length=100)
    batch_of = models.CharField(max_length=4, default='2015')

    def get_absolute_url(self):
        return "https://fb.com/profile.php?id=" + self.fb_id

    def get_picture(self):
        text = requests.get('https://fb.com/profile.php?id=' + self.fb_id).text
        if text.find('profilePic img') != -1:
            # There is a profile pic
            x = text.find('src', text.find('profilePic img'))
            link = text[x:text.find('"', x+5)]
            link = link[5:]
            if self.fb_image_url != link:
                self.fb_image_url=link
        return self.fb_image_url


class Variable(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
