# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('orfik', '0005_auto_20170127_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_solve',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 27, 1, 46, 51, 143522)),
        ),
    ]
