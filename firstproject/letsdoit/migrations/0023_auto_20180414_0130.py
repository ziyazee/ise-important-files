# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-13 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('letsdoit', '0022_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='categorie',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='letsdoit.clasyear', to_field='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='fdescription',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]