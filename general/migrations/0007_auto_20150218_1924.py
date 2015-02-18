# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_compmember_batch_of'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteVisit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('users', models.IntegerField(default=0)),
                ('auth_access', models.IntegerField(default=0)),
                ('access_count', models.IntegerField(default=1)),
                ('last_count', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='track',
            name='ip',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
