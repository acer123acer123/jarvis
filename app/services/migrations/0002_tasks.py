# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('action_word', models.CharField(max_length=100)),
                ('cmd', models.CharField(max_length=100, verbose_name=b'command script')),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
