# Generated by Django 3.1.7 on 2021-04-19 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0003_auto_20210419_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavepermission',
            name='duration',
        ),
    ]
