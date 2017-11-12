# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0018_post_not_sub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='not_sub',
            new_name='is_main',
        ),
    ]
