from django.db import models
from django.utils.timezone import now
from home_main.models import ProductDetails
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.
order_status = (
    ("Ordered", "Ordered"),
    ("Accepted", "Accepted"),
    ("Cancelled", "Cancelled"),
    ("Rejected", "Rejected"),
    ("Returned", "Returned"),
    ("Refunded", "Refunded"),

)


class cart_items(models.Model):
    userid = models.IntegerField()
    prod_id = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal = models.IntegerField()
    wishlist = models.BooleanField(default=False)


class orderlist_details(models.Model):
    orderid = models.IntegerField()
    orderdate = models.DateTimeField(default=now)
    userid = models.IntegerField()
    prod_id = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    subtotal = models.IntegerField()
    status = models.IntegerField(default=1)


class wishlist_items(models.Model):
    userid = models.IntegerField()
    prod_id = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)


class Final_Order_Table(models.Model        ):
    # orderid = models.ForeignKey(orderlist_details,on_delete=models.CASCADE)
    orderid = models.IntegerField()
    userid = models.IntegerField()
    deliver_date = models.DateField()
    address = models.TextField()
    town = models.CharField(max_length=30)
    postcode = models.CharField(max_length=6)
    phone = PhoneNumberField()
    order_notes = models.TextField()
    total_price = models.IntegerField()
    advance_amount = models.IntegerField()
    balance_amount = models.IntegerField()
    no_of_products = models.IntegerField(null=True)
    status = models.CharField(max_length=20, choices=order_status)

    def __str__(self):
        return str(self.orderid) + "   " + str(self.userid) + "  " + str(self.no_of_products)


