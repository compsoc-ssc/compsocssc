# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('orfik', '0006_auto_20170127_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_solve',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 27, 1, 48, 8, 843466)),
        ),
    ]
