from django.db import models

class CompMember(models.Model):
    """A member of compsoc"""
    fb_id=models.CharField(max_length=20,help_text='facebook id number.')
    fb_image_url=models.TextField()#field for picture
    name=models.CharField(max_length=20)
    alumni=models.Booleanfield(default=False)
    role=models.CharField(max_length=100)#what role do they have in compsoc
    def get_absolute_url(self):
        return "https://fb.com/profile.php?id="+self.fb_id
    def get_picture(self):
        #check if picture changed
        return self.fb_image_url
