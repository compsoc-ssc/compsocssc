# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participation_method',
            field=models.CharField(max_length=20, choices=[('IN', 'Individual'), ('INORTEAMS2', 'Individual or Teams of 2'), ('TEAMS2', 'Teams of 2'), ('TEAMS2PLUS', 'Teams of 2 or more')], default='IN'),
            preserve_default=True,
        ),
    ]
