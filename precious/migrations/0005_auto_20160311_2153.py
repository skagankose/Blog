# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0004_post_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalfile',
            name='height',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='generalfile',
            name='width',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
