# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0006_auto_20160311_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_editor',
            field=models.BooleanField(default=False),
        ),
    ]
