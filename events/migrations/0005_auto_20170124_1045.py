# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20160313_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='appname',
            field=models.CharField(default='orfik', help_text='The name must be known to the app which handles this event. For example orfik', max_length=120),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(help_text='This is the public name of the app. For exmaple Orfik 2055', max_length=120),
        ),
    ]
