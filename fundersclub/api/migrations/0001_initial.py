# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bank_account_number', models.IntegerField()),
                ('companies', models.CharField(max_length=100)),
                ('is_single_asset', models.BooleanField()),
                ('legal_name', models.CharField(max_length=100)),
                ('llc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Llc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateField()),
                ('dissolved', models.BooleanField()),
                ('legal_name', models.CharField(max_length=100)),
            ],
        ),
    ]
