# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import oauth2client.contrib.django_util.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('orfik', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('credentials', oauth2client.contrib.django_util.models.CredentialsField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='last_solve',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 26, 22, 41, 57, 330353)),
        ),
    ]
