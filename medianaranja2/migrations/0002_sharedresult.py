# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-16 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('medianaranja2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.UUIDField(default=uuid.uuid4)),
                ('data', picklefield.fields.PickledObjectField(editable=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
