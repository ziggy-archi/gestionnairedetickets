# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nom', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('demandes', models.CharField(max_length=200)),
                ('cloture_du_ticket', models.BooleanField(default=False)),
                ('date_de_soumission', models.DateTimeField()),
                ('personne', models.ForeignKey(to='oob.Personne')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
