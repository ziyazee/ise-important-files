# Generated by Django 2.0.3 on 2018-04-03 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsdoit', '0004_auto_20180402_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('legs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='birds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('legs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='livings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
