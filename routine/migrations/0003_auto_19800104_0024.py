# Generated by Django 3.1.7 on 1980-01-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0002_auto_20210415_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dutyrota',
            options={'verbose_name_plural': 'Duty Rotas'},
        ),
        migrations.RemoveField(
            model_name='dutyrota',
            name='Month',
        ),
        migrations.RemoveField(
            model_name='dutyrota',
            name='day',
        ),
        migrations.RemoveField(
            model_name='dutyrota',
            name='week_number',
        ),
        migrations.AddField(
            model_name='dutyrota',
            name='date',
            field=models.DateField(default='2021-01-13'),
            preserve_default=False,
        ),
    ]
