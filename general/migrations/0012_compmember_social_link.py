# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_auto_20150829_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='compmember',
            name='social_link',
            field=models.CharField(default='javascript:void(0)', max_length=256),
            preserve_default=True,
        ),
    ]
