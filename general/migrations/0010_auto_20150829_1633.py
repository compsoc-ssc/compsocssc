# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20150828_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compmember',
            name='fb_id',
        ),
        migrations.RemoveField(
            model_name='compmember',
            name='fb_image_url',
        ),
        migrations.AddField(
            model_name='compmember',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '500x500', free_crop=False, verbose_name='cropping', allow_fullsize=False, size_warning=False, adapt_rotation=False, hide_image_field=False, help_text=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compmember',
            name='image',
            field=models.ImageField(blank=True, upload_to='member_images'),
            preserve_default=True,
        ),
    ]
