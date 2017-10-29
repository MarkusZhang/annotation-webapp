# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20170917_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='is_labeling_finished',
        ),
        migrations.AddField(
            model_name='product',
            name='is_labeling_finished',
            field=models.BooleanField(default=False),
        ),
    ]
