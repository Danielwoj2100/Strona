# Generated by Django 3.1.7 on 2021-03-29 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0010_auto_20210329_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='kurs',
            field=models.ForeignKey(db_column='nazwa', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='links.kurs'),
        ),
        migrations.AddField(
            model_name='kurs',
            name='kategoria',
            field=models.ForeignKey(db_column='nazwa_kategorii', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='links.kategoria'),
        ),
    ]