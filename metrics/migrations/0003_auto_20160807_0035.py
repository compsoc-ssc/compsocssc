# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_hit_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hit',
            name='url',
            field=models.CharField(default='/', max_length=500),
            preserve_default=True,
        ),
    ]
