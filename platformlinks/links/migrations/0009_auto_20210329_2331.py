# Generated by Django 3.1.7 on 2021-03-29 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0008_film_kategoria_kurs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='kurs',
        ),
        migrations.RemoveField(
            model_name='kurs',
            name='kategoria',
        ),
    ]
