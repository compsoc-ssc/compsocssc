# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_auto_20150829_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compmember',
            name='image',
            field=models.ImageField(upload_to='static/images/member_images'),
            preserve_default=True,
        ),
    ]
