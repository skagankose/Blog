# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('position', models.IntegerField(default=9999)),
                ('file_item', models.FileField(blank=True, upload_to='file/')),
                ('image', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('other', models.BooleanField(default=False)),
                ('edited', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='GeneralText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('position', models.IntegerField(default=9999)),
                ('text', models.TextField()),
                ('paragraph', models.BooleanField(default=False)),
                ('heading', models.BooleanField(default=False)),
                ('subheading', models.BooleanField(default=False)),
                ('subsubheading', models.BooleanField(default=False)),
                ('list_item', models.BooleanField(default=False)),
                ('inline_block', models.BooleanField(default=False)),
                ('code', models.BooleanField(default=False)),
                ('table', models.BooleanField(default=False)),
                ('link', models.BooleanField(default=False)),
                ('youtube', models.BooleanField(default=False)),
                ('edited', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('thumbnail', models.ImageField(blank=True, upload_to='img/')),
                ('item_position', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(related_name='posts', to='precious.Category', blank=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.AddField(
            model_name='generaltext',
            name='post',
            field=models.ForeignKey(to='precious.Post', related_name='general_texts'),
        ),
        migrations.AddField(
            model_name='generalfile',
            name='post',
            field=models.ForeignKey(to='precious.Post', related_name='general_files'),
        ),
    ]
