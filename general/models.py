from django.db import models
from django.conf import settings
import requests

class CompMember(models.Model):
    """A member of compsoc"""
    fb_id=models.CharField(max_length=20,help_text='facebook id number.')
    fb_image_url=models.TextField()#field for picture
    name=models.CharField(max_length=20)
    alumni=models.BooleanField(default=False)
    role=models.CharField(max_length=100)#what role do they have in compsoc
    batch_of=models.CharField(max_length=4,default='2015')
    def get_absolute_url(self):
        return "https://fb.com/profile.php?id="+self.fb_id
    def get_picture(self):
        text=requests.get('https://fb.com/profile.php?id='+self.fb_id).text
        if text.find('profilePic img')!=-1:
            #there is a profile pic
            x=text.find('src',text.find('profilePic img'))
            link=text[x:text.find('"',x+5)]
            link=link[5:]
            if self.fb_image_url!=link:self.fb_image_url=link
        return self.fb_image_url
class Variable(models.Model):
    name=models.CharField(max_length=100)
    time=models.DateTimeField()
class Track(models.Model):
    def __str__(self):return self.ip
    ip=models.CharField(max_length=100)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='track',null=True)
    url=models.CharField(max_length=200,default='unknown')
    agent=models.CharField(max_length=200,default='unknown')
    time=models.DateTimeField(auto_now_add=True)
