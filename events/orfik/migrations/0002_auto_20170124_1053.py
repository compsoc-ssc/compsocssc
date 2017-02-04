# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20170124_1045'),
        ('orfik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='stamp',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='question',
            name='event',
            field=models.ForeignKey(to='events.Event', related_name='event_question', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='last_solve',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
