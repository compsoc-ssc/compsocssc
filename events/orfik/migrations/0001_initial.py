# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=100)),
                ('correct', models.NullBooleanField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=20)),
                ('max_level', models.SmallIntegerField(default=0)),
                ('last_solve', models.DateTimeField(default=datetime.datetime(2017, 1, 9, 15, 24, 43, 245795))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('number', models.SmallIntegerField()),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='question')),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='attempt',
            name='player',
            field=models.ForeignKey(to='orfik.Player', related_name='player_attempt'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='question',
            field=models.ForeignKey(to='orfik.Question', related_name='attempt'),
        ),
    ]
