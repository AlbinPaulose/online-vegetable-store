# Generated by Django 3.1.5 on 2021-07-31 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer_activity', '0014_auto_20210731_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist_details',
            name='orderdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
