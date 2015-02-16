# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompMember',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('fb_id', models.CharField(max_length=20, help_text='facebook id number.')),
                ('fb_image_url', models.TextField()),
                ('name', models.CharField(max_length=20)),
                ('alumni', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
