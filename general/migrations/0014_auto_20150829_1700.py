# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0013_auto_20150829_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compmember',
            name='image',
            field=models.ImageField(upload_to='static/images/member_images', help_text='Please select a display image for yourself. This is necessary.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='compmember',
            name='name',
            field=models.CharField(max_length=50, help_text='Enter your full name'),
            preserve_default=True,
        ),
    ]
