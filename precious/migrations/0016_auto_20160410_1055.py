# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0015_auto_20160410_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='not a Sub-Post',
            new_name='not_sub',
        ),
    ]
