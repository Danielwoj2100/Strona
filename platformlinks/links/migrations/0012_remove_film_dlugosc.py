# Generated by Django 3.1.7 on 2021-04-21 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0011_auto_20210329_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='dlugosc',
        ),
    ]
