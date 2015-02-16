# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='agent',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='track',
            name='url',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=True,
        ),
    ]
