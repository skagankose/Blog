# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0016_auto_20160410_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='not_sub',
        ),
    ]
