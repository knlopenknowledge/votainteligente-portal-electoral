# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-15 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merepresenta', '0016_auto_20180809_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='LGBTQDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nome')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='lgbt_desc',
            field=models.ManyToManyField(to='merepresenta.LGBTQDescription'),
        ),
    ]
