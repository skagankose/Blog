# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0013_post_is_external'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_external',
            field=models.BooleanField(default=False),
        ),
    ]
