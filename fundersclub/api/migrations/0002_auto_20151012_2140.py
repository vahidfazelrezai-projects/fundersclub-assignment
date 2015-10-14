# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.RemoveField(
            model_name='fund',
            name='companies',
        ),
        migrations.AddField(
            model_name='fund',
            name='companies',
            field=models.ManyToManyField(to='api.Company'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='llc',
            field=models.ForeignKey(to='api.Llc'),
        ),
        migrations.AlterField(
            model_name='llc',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
