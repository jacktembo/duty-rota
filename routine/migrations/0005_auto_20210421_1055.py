# Generated by Django 3.1.7 on 2021-04-21 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dutyrota', '0002_auto_20210421_1055'),
        ('routine', '0004_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='target_audience',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='')),
                ('headteacher', models.CharField(max_length=50)),
                ('website', models.CharField(blank=True, max_length=64, null=True)),
                ('facebook', models.URLField(max_length=255)),
                ('twitter', models.URLField(blank=True, max_length=255, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dutyrota.address')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
