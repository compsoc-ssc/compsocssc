from django.db import models
from django.utils import timezone
from django.conf import settings
import requests


USER = settings.AUTH_USER_MODEL

class CompMember(models.Model):
    """A member of compsoc"""
    fb_id = models.CharField(max_length=20, help_text='Facebook id number.')
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


class Track(models.Model):
    def __str__(self):
        return self.ip
    ip = models.CharField(max_length=20)
    user = models.ForeignKey(USER, related_name='track', null=True)
    url = models.CharField(max_length=200, default='unknown')
    agent = models.CharField(max_length=200, default='unknown')
    time=models.DateTimeField(auto_now_add=True)


class SiteVisit(models.Model):
    def __str__(self):
        return self.ip
    # what ip address
    ip = models.GenericIPAddressField(unique=True)
    # which users
    users = models.IntegerField(default=0)
    # how many logged in access
    auth_access = models.IntegerField(default=0)
    # how many accesses
    access_count = models.IntegerField(default=1)
    last_count = models.DateTimeField(auto_now=True)
    def __count_total(self):
        if (timezone.now()-self.last_count).total_seconds() > 20:
            total = Track.objects.filter(ip=self.ip).count()
            not_access = Track.objects.filter(ip=self.ip, user=None).count()
            self.access_count = total
            self.auth_access = total - not_access
            self.save()

    def logged_in_access(self):
        self.__count_total()
        return self.auth_access

    def total_access(self):
        self.__count_total()
        return self.access_count
