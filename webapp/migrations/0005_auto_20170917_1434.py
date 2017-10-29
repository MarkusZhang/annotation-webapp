# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20170917_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerimage',
            options={'ordering': ['pk']},
        ),
        migrations.RemoveField(
            model_name='labeledby',
            name='customer_image',
        ),
        migrations.AddField(
            model_name='labeledby',
            name='product',
            field=models.ForeignKey(null=True, to='webapp.Product'),
        ),
    ]
