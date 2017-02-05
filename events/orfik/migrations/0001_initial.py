# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0006_auto_20170204_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('correct', models.NullBooleanField(default=None)),
                ('stamp', models.DateTimeField(null=True, auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('max_level', models.SmallIntegerField(default=0)),
                ('last_solve', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('number', models.SmallIntegerField()),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='question', null=True)),
                ('answer', models.CharField(max_length=100)),
                ('event', models.ForeignKey(related_name='event_question', to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='attempt',
            name='player',
            field=models.ForeignKey(related_name='player_attempt', to='orfik.Player'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='question',
            field=models.ForeignKey(related_name='attempt', to='orfik.Question'),
        ),
    ]
