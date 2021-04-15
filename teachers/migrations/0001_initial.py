# Generated by Django 3.1.7 on 2021-04-15 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dutyrota', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('other_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('nrc', models.CharField(max_length=12)),
                ('birth_date', models.DateField()),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dutyrota.gender')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teachers.person')),
                ('phone_number', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=64)),
            ],
            bases=('teachers.person',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('teacher_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='teachers.teacher')),
            ],
            bases=('teachers.teacher',),
        ),
    ]
