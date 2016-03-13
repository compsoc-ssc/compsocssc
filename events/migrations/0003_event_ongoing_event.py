# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160313_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ongoing_event',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
