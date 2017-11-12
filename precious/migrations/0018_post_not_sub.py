# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('precious', '0017_remove_post_not_sub'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='not_sub',
            field=models.BooleanField(default=True),
        ),
    ]
