# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-09 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0008_quotation_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='statut',
            field=models.CharField(choices=[('PROGRESS', 'In progress'), ('RECALL', 'In recall'), ('DONE', 'Done')], default=None, max_length=20),
        ),
    ]
