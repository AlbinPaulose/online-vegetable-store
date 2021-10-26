from django.db import models

# Create your models here.
priceunits = (
        ("1 kg","1 Kg"),
        ("1 piece","1 Piece"),
        ("1 bunch","1 Bunch"),
        ("100 mg","100 mg")
    )
class ProductDetails(models.Model):
    prodname = models.CharField(max_length=50)
    prodpriceunit = models.CharField(max_length=20,choices=priceunits,default='1 Kg')
    prodprice = models.IntegerField()
    prodstock = models.IntegerField()
    prodcategory = models.CharField(max_length=100)
    addondate = models.DateTimeField()
    prodoffer = models.BooleanField(default=False)
    prodofferdetails = models.TextField()
    prodimage = models.ImageField(upload_to='product images')
    prodselected = models.IntegerField(default=0)  #the no. of times were users choosed to buy this product, in order to give suggestion for most selled products.

    def __str__(self):
        return self.prodname + " " + self.prodpriceunit

