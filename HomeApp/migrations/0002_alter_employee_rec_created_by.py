# Generated by Django 4.2 on 2023-09-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='rec_created_by',
            field=models.DateField(auto_now=True),
        ),
    ]
