# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oob', '0002_auto_20150330_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='personne',
            field=models.ForeignKey(default=None, null=True, to='oob.Personne'),
            preserve_default=True,
        ),
    ]
