# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0007_post_is_editor'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_black',
            field=models.BooleanField(default=False),
        ),
    ]
