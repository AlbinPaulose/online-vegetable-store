# Generated by Django 3.1.5 on 2021-07-26 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_main', '0002_auto_20210705_2107'),
        ('customer_activity', '0011_final_order_table_no_of_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist_details',
            name='prod_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_main.productdetails'),
        ),
    ]