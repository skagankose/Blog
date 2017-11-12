# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0012_generaltext_is_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_external',
            field=models.BooleanField(default=True),
        ),
    ]
