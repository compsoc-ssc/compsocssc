# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_track_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='compmember',
            name='batch_of',
            field=models.CharField(default='2015', max_length=4),
            preserve_default=True,
        ),
    ]
