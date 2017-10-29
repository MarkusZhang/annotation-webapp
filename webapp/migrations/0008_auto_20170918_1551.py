# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20170917_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerimage',
            name='times_labeled',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customerimage',
            name='image_path',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image_path',
            field=models.TextField(unique=True),
        ),
    ]
