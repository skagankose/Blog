# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0019_auto_20160429_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_main',
        ),
    ]
