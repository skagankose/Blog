# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0011_auto_20160409_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaltext',
            name='is_index',
            field=models.BooleanField(default=False),
        ),
    ]
