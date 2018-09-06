# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-03 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0034_auto_20180903_1614'),
        ('merepresenta', '0018_auto_20180830_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='RightAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidator.Position')),
                ('topic', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_answer', to='elections.Topic')),
            ],
        ),
    ]
