# Generated by Django 2.1.5 on 2020-03-08 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='fotografia',
        ),
    ]
