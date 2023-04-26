# Generated by Django 3.2.12 on 2023-04-26 01:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('number_of_employees', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='access_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='accessrecord',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=264, unique=True)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.company')),
            ],
        ),
    ]
