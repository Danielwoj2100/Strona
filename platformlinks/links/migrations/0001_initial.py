# Generated by Django 3.1.7 on 2021-03-29 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'kursy',
                'db_table': 'kursy',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('hiperlacze', models.CharField(max_length=256)),
                ('tutul', models.CharField(max_length=256)),
                ('dlugosc', models.BigIntegerField()),
                ('kurs', models.ForeignKey(db_column='nazwa', on_delete=django.db.models.deletion.DO_NOTHING, to='links.kurs')),
            ],
            options={
                'verbose_name_plural': 'filmy',
                'db_table': 'filmy',
                'managed': True,
            },
        ),
    ]
