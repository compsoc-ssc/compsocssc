# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewMember',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50, choices=[('ECO', 'B.A. Economics(Hons.)'), ('ENG', 'B.A. English(Hons.)'), ('HIS', 'B.A. History(Hons.)'), ('PHI', 'B.A. Philosophy(Hons.)'), ('SAN', 'B.A. Sanskrit(Hons.)'), ('BAP', 'B.A. Programme'), ('MAT', 'B.Sc. Mathematics(Hons.)'), ('CHM', 'B.Sc. Chemistry(Hons.)'), ('PHY', 'B.Sc. Physics(Hons.)'), ('BCM', 'B.Sc. Programme(Chemistry)'), ('BCS', 'B.Sc. Programme(Computer Science)')])),
                ('year', models.PositiveSmallIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three')])),
                ('phone_number', models.CharField(validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits.', regex='^\\d{10}$')], max_length=10)),
                ('email', models.EmailField(max_length=75)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
