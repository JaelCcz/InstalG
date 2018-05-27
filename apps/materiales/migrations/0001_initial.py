# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-22 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('existencia', models.IntegerField()),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
    ]