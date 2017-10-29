# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_time_label',
            field=models.DateTimeField(null=True),
        ),
    ]
