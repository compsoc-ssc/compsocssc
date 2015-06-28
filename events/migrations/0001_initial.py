# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('fb_event_page', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=30)),
                ('participation_method', models.CharField(default='IN', max_length=20, choices=[('IN', 'Individual'), ('TEAMS2', 'Teams of 2'), ('TEAMS2PLUS', 'Teams of 2 or more')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
