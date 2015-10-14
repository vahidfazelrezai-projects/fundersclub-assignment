# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151012_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='llc',
            field=models.ForeignKey(related_name='funds', to='api.Llc'),
        ),
    ]
