from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductDetails

# Create your views here.

'''Intial Home Page'''
def index(request):
    products = ProductDetails.objects.all()
    latestproducts = ProductDetails.objects.order_by('-addondate')[:5]
    return render(request, "index.html", {'products': products,'recentproducts':latestproducts})