# Generated by Django 3.1.7 on 2021-04-21 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0012_remove_film_dlugosc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='tutul',
            new_name='tytul',
        ),
    ]