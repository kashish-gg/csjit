# Generated by Django 4.0.3 on 2022-05-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_accountno_post_amount_paid_post_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='emailid',
            field=models.CharField(default='---', max_length=35),
        ),
    ]
