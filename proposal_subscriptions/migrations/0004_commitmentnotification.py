# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-14 18:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('popular_proposal', '0027_auto_20170914_1841'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proposal_subscriptions', '0003_auto_20170817_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitmentNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notified', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('commitment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='popular_proposal.Commitment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commitment_notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
