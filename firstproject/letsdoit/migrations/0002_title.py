# Generated by Django 2.0.3 on 2018-04-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsdoit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=50)),
                ('exp', models.CharField(max_length=20)),
            ],
        ),
    ]
