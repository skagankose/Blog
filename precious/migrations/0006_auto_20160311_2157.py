# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0005_auto_20160311_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalfile',
            name='height',
        ),
        migrations.RemoveField(
            model_name='generalfile',
            name='width',
        ),
    ]
