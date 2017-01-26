# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0016_auto_20150829_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='compmember',
            name='index',
            field=models.IntegerField(default=-1, help_text='This field is present just for ordering members based on their posts. President = 2, VPs = 1, Gen. Sec. = 0, Everyone else = -1'),
        ),
    ]
