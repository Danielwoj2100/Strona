# Generated by Django 3.1.7 on 2021-03-29 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_auto_20210329_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_kategorii', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'kategorie',
                'db_table': 'kategorie',
            },
        ),
        migrations.AddField(
            model_name='kurs',
            name='kategoria',
            field=models.ForeignKey(db_column='nazwa_kategorii', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='links.kategoria'),
        ),
    ]
