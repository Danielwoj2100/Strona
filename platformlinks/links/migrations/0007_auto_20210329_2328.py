# Generated by Django 3.1.7 on 2021-03-29 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_auto_20210329_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurs',
            name='kategoria',
        ),
        migrations.DeleteModel(
            name='Film',
        ),
        migrations.DeleteModel(
            name='Kategoria',
        ),
        migrations.DeleteModel(
            name='Kurs',
        ),
    ]
