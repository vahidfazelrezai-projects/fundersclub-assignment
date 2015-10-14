# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_company_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='display_name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fund',
            name='legal_name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fund',
            name='llc',
            field=models.ForeignKey(to='api.Llc', to_field=b'legal_name'),
        ),
        migrations.AlterField(
            model_name='llc',
            name='legal_name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
