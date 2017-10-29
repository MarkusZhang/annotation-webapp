# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20170917_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.AddField(
            model_name='customerimage',
            name='image_path',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimage',
            name='image_path',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
