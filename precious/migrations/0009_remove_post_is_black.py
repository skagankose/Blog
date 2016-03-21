# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0008_post_is_black'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_black',
        ),
    ]
