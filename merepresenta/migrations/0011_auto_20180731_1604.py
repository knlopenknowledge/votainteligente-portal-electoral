# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-31 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merepresenta', '0010_volunteerprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteergetscandidateemaillog',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend_candidate.CandidacyContact'),
        ),
    ]
