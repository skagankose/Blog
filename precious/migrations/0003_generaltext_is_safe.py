# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0002_auto_20150929_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaltext',
            name='is_safe',
            field=models.BooleanField(default=False),
        ),
    ]
