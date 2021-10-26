# Generated by Django 3.1.5 on 2021-07-10 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer_activity', '0005_cart_items_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderlist_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.IntegerField()),
                ('orderdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('userid', models.IntegerField()),
                ('prod_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('subtotal', models.IntegerField()),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]