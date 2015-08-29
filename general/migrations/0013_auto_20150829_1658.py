# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_compmember_social_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compmember',
            name='alumni',
            field=models.BooleanField(help_text='Are you an alumni?', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='compmember',
            name='batch_of',
            field=models.CharField(max_length=4, help_text='Enter the year you will graduate', default='2015'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='compmember',
            name='role',
            field=models.CharField(max_length=100, help_text="Enter your post if you hold one. If not, enter 'Member'"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='compmember',
            name='social_link',
            field=models.CharField(max_length=256, help_text='Enter a link to your Facebook, Twitter, GitHub or any other social network profile'),
            preserve_default=True,
        ),
    ]
