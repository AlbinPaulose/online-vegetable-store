# Generated by Django 3.1.5 on 2021-07-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_activity', '0008_final_order_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='final_order_table',
            name='orderid',
            field=models.IntegerField(),
        ),
    ]