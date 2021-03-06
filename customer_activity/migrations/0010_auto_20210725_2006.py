# Generated by Django 3.1.5 on 2021-07-25 14:36

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('customer_activity', '0009_auto_20210725_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='final_order_table',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='final_order_table',
            name='postcode',
            field=models.CharField(max_length=6),
        ),
    ]
