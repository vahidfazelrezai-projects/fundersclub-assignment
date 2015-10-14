# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151014_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='companies',
            field=models.ManyToManyField(related_name='funds', to='api.Company'),
        ),
    ]
