# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0003_auto_20160807_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newmember',
            name='email',
            field=models.EmailField(unique=True, max_length=254, error_messages={'unique': 'This email has already been registered.'}),
        ),
    ]
