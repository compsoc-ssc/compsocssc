# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newmember',
            name='course',
            field=models.CharField(choices=[('ECO', 'B.A. Economics (Hons.)'), ('ENG', 'B.A. English (Hons.)'), ('HIS', 'B.A. History (Hons.)'), ('PHI', 'B.A. Philosophy (Hons.)'), ('SAN', 'B.A. Sanskrit (Hons.)'), ('BAP', 'B.A. Programme'), ('MAT', 'B.Sc. Mathematics (Hons.)'), ('CHM', 'B.Sc. Chemistry (Hons.)'), ('PHY', 'B.Sc. Physics (Hons.)'), ('BCM', 'B.Sc. Programme (Chemistry)'), ('BCS', 'B.Sc. Programme (Computer Science)')], max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newmember',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newmember',
            name='year',
            field=models.PositiveSmallIntegerField(choices=[(1, 'One (I)'), (2, 'Two (II)'), (3, 'Three (III)')]),
            preserve_default=True,
        ),
    ]
