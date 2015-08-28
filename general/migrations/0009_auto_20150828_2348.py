# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_auto_20150628_1417'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SiteVisit',
        ),
        migrations.RemoveField(
            model_name='track',
            name='user',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
