# Generated by Django 4.0.3 on 2022-05-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_dates_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]