# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hit',
            name='url',
            field=models.CharField(default=b'/', max_length=500),
            preserve_default=True,
        ),
    ]
