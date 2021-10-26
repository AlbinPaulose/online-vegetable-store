# Generated by Django 3.2.3 on 2021-07-01 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('prod_id', models.IntegerField()),
                ('prodname', models.CharField(max_length=50)),
                ('prodpriceunit', models.CharField(max_length=20)),
                ('prodprice', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('wishlist', models.BooleanField()),
            ],
        ),
    ]
