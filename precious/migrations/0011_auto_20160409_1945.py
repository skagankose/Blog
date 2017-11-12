# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0010_auto_20160321_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='not_sub',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_editor',
            field=models.BooleanField(default=True),
        ),
    ]
