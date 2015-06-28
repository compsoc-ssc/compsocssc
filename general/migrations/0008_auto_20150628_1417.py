# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_auto_20150218_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compmember',
            options={'verbose_name': 'CompSoc Member', 'verbose_name_plural': 'CompSoc Members'},
        ),
        migrations.AlterField(
            model_name='compmember',
            name='fb_id',
            field=models.CharField(max_length=20, help_text='Facebook ID:'),
            preserve_default=True,
        ),
    ]
