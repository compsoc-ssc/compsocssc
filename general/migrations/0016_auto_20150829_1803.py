# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0015_auto_20150829_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compmember',
            name='image',
            field=models.ImageField(help_text='Please select a display image for yourself. This is necessary.', upload_to='member_images/'),
            preserve_default=True,
        ),
    ]
