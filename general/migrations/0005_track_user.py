# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0004_auto_20150216_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='user',
            field=models.ForeignKey(null=True, related_name='track', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
