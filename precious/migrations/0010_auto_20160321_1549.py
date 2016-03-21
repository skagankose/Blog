# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0009_remove_post_is_black'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generaltext',
            name='table',
        ),
        migrations.RemoveField(
            model_name='generaltext',
            name='youtube',
        ),
    ]
