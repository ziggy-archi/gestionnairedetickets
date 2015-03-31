# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='courriel',
            field=models.CharField(null=True, max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='demandeur',
            field=models.CharField(null=True, max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='demandes',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
    ]
