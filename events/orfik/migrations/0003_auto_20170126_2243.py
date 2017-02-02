# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('orfik', '0002_auto_20170126_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_solve',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 26, 22, 43, 8, 77513)),
        ),
    ]
