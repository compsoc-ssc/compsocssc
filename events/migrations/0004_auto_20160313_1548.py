# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_ongoing_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ongoing_event',
            field=models.BooleanField(help_text='Check this if this event spans over multiple days', default=False),
            preserve_default=True,
        ),
    ]
