# Generated by Django 2.0.3 on 2018-04-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsdoit', '0002_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='exp',
            field=models.IntegerField(max_length=20),
        ),
    ]
