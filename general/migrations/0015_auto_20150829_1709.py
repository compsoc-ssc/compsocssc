# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0014_auto_20150829_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compmember',
            name='image',
            field=models.ImageField(upload_to='/member_images', help_text='Please select a display image for yourself. This is necessary.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='compmember',
            name='social_link',
            field=models.CharField(help_text='Enter a link to your Facebook, Twitter, GitHub or any other social network profile. You can leave this blank if you wish!', max_length=256, blank=True),
            preserve_default=True,
        ),
    ]
