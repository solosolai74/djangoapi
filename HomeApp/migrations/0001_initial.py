# Generated by Django 4.2 on 2023-09-10 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('rec_created_by', models.DateField()),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('remarks', models.CharField(blank=True, max_length=1000, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
