# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-04 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='slug',
            field=models.SlugField(default='plop'),
            preserve_default=False,
        ),
    ]
