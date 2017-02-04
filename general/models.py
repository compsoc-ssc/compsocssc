from django.db import models
import warnings
from django.utils import timezone
import requests

from image_cropping import ImageRatioField

class CompMember(models.Model):
    """A member of compsoc"""

    class Meta:
        verbose_name = 'CompSoc Member'
        verbose_name_plural = 'CompSoc Members'

    index = models.IntegerField(blank=False, help_text="This field is present just for ordering members based on their posts. President = 2, VPs = 1, Gen. Sec. = 0, Everyone else = -1", default=-1)
    name = models.CharField(max_length=50, help_text='Enter your full name')

    image = models.ImageField(blank=False, upload_to='member_images/', help_text='Please select a display image for yourself. This is necessary.')
    cropping = ImageRatioField('image', '500x500')

    alumni = models.BooleanField(default=False, help_text='Are you an alumni?')
    role = models.CharField(max_length=100, help_text="Enter your post if you hold one. If not, enter 'Member'")
    batch_of = models.CharField(max_length=4, default='2015', help_text='Enter the year you will graduate')
    social_link = models.CharField(blank=True, max_length=256, help_text='Enter a link to your Facebook, Twitter, GitHub or any other social network profile. You can leave this blank if you wish!')

    def get_social_link(self):
        '''
        Returns the social_link if present. Otherwise, sends javascript:void(0)
        '''
        if self.social_link == '':
            return 'javascript:void(0)'
        else:
            return self.social_link

    def __str__(self):
        return self.name


class Variable(models.Model): ##NOTE: This should not be used anymore
    def __str__(self):
        warnings.warn('''You are using a "General Variable".
        Stop doing that.
        This is bad design on Arjoonn's part so don't fall into the same trap.
        If you are using this for Orfik, that has already been fixed. If you are using this for logos, same thing.

        Over a few cycles this entire table will be removed.
        ''')
        return self.name
    name = models.CharField(max_length=100)
    time = models.DateTimeField()


# Receive the pre_delete signal and delete the image associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=CompMember)
def compsoc_member_delete(sender, instance, **kwargs):
    # Pass false so ImageField doesn't save the model.
    instance.image.delete(False)
