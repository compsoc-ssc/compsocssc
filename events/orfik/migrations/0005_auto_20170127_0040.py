# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('orfik', '0004_auto_20170126_2311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credentialsmodel',
            old_name='credentials',
            new_name='credential',
        ),
        migrations.AlterField(
            model_name='credentialsmodel',
            name='id',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_solve',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 27, 0, 40, 18, 613383)),
        ),
    ]
