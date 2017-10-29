# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('label_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LabeledBy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('record_time', models.DateTimeField(blank=True, null=True)),
                ('customer_image', models.ForeignKey(to='webapp.CustomerImage')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('is_labeling_finished', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='webapp.Product')),
            ],
        ),
        migrations.AddField(
            model_name='customerimage',
            name='product',
            field=models.ForeignKey(to='webapp.Product'),
        ),
    ]
