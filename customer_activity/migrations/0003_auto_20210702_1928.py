# Generated by Django 3.2.3 on 2021-07-02 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_activity', '0002_alter_cart_items_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_items',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart_items',
            name='wishlist',
            field=models.BooleanField(default=False),
        ),
    ]
