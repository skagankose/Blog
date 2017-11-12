# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0014_auto_20160409_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='not_sub',
            new_name='not a Sub-Post',
        ),
    ]
