from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, request
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import  cart_items,orderlist_details,wishlist_items
from .models import*
from home_main.models import ProductDetails
from login.views import cart_items_counts,wishlist_counts
from  django.contrib.auth.models import  User, auth


# Create your views here.
"""
    MY ORDER DETAILS
"""


def my_orders(request):
    userid = request.session['userid']
    items = Final_Order_Table.objects.filter(userid=userid).order_by('-orderid')
    if items is not None:
        for orders in items:
            if orders.orderid is not None:
                return render(request,'my_orders.html',{'orders':items})
        messages.info(request, 'Not Yet Ordered Anything!!!')
        return render(request, 'my_orders.html')



"""
    VIEW ALL ORDER DETAILS
"""


def view_order_details(request,orderid,total_price,adv_amount,bal_amount,status):
    userid = request.session['userid']
    items = orderlist_details.objects.filter(orderid=orderid,userid=userid)
    return render(request,'my_order_details.html',{'items':items,'total_price':total_price,'advance_amount':adv_amount,'balance_amount':bal_amount,'status':status})


"""
    CANCEL ORDER IS AFTER PAYING ADVACNCE AMOUNT WHICH IS CHANGING THE STATUS IN final_order_table
"""


def cancel_order(request,orderid):
    userid = request.session['userid']
    item = Final_Order_Table.objects.filter(orderid=orderid,userid=userid).update(status='Cancelled')
    #item.status = 'Cancelled'
    #item.save();
    return redirect('my_orders')


"""
    VIEWING CART LIST 
"""


def shoppingcart(request):
    cart_items_counts(request)
    cartitems_count = request.session['count_cartitems']
    totals = {}
    userid = request.session['userid']
    items = cart_items.objects.filter(userid=userid).order_by('-id')
    if items is not None:
        for product in items:
            productid = product.prod_id.id
            if productid is not None:
                placeorder(request)
                subtotal = request.session['subtotal']
                totals['subtotal'] = subtotal
                return render(request, "shoping-cart.html", {'products': items, 'subtotal': subtotal,'cartitems_count':cartitems_count})
            else:
                return render(request, "shoping-cart.html", {'products': items,'cartitems_count':cartitems_count})
    else:
        return render(request, "shoping-cart.html", {'products': items})
    return render(request, "shoping-cart.html", {'products': items})



"""
    ADDING PRODUCTS TO cart_items TABLE
"""


def addcart(request, prodid, userid, ):
    productid = ProductDetails.objects.get(id=prodid)
    price = productid.prodprice
    if cart_items.objects.filter(userid=userid, prod_id=productid).exists():
        print("Item already added")
    else:
        items = cart_items.objects.create(userid=userid, prod_id=productid, subtotal = price)
        items.save();
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('users_home')

def cartbutton(request,prodid,userid):
    data = {}
    productid = ProductDetails.objects.get(id=prodid)
    if cart_items.objects.filter(userid=userid, prod_id=productid).exists():
        val = 1
        data['val'] = 1
        print("Yes...............")
    else:
        data['val'] = 0
        print('no.................')



"""
    DELETE PRODUCTS FROM CART
"""


def deletecart(request, prodid):
    productid =prodid
    userid = request.session['userid']
    item = cart_items.objects.filter(userid=userid,prod_id=productid)
    item.delete()
    return redirect('shoppingcart')


"""
    UPDATE QUANTITY
"""
def updatequantity(request):
    #if request.method == 'POST':
    userid = request.session['userid']
    quantity = request.POST['qty']
    productid = request.POST['productid']
    product = ProductDetails.objects.get(id=productid)
    price = product.prodprice
    if int(quantity) > 1:
        subtotal = int(quantity) * int(price)
        cart_items.objects.filter(userid=userid, prod_id=productid).update(quantity=quantity,subtotal=subtotal)
    else:
        messages.info(request, 'Enter a valid quantity!')
    return redirect('shoppingcart')


"""
    BELOW FUNCTION IS TO CALCULATE THE TOTAL SUM OF ALL PRODUCTS IN CART
"""
def placeorder(request):
    subtotal=0
    totals = {}
    total =0
    userid = request.session['userid']
    items = cart_items.objects.filter(userid=userid)
    for product in items:
        price = product.prod_id.prodprice
        quantity = product.quantity
        subtotal= price*quantity
        total += subtotal
    totals['subtotal'] = total
    request.session['subtotal'] = total
    #return redirect('shoppingcart')


""" 
    ORDER THE PRODUCTS IN THE CART AND SAVE TO THE orderlist_details TABLE
"""
def orderproducts(request):
    ttotal =0
    total = request.session['subtotal']
    orderlist = orderlist_details.objects.order_by('orderid').last()
    if orderlist is None:
        orderid = 1
    else:
        orderid = orderlist.orderid + 1
    userid = request.session['userid']
    productslist = cart_items.objects.filter(userid=userid)
    for product in productslist:
        product_id = ProductDetails.objects.get(id=product.prod_id.id)
        price = product.prod_id.prodprice
        quantity = product.quantity
        subtotal = product.subtotal
        ttotal += subtotal
        item = orderlist_details.objects.create(orderid=orderid,userid=userid,prod_id=product_id,quantity=quantity,price=price,subtotal=subtotal)
        item.save();
    advance_amount = (ttotal*10) // 100
    balance_amount = ttotal - advance_amount
    userdetails = User.objects.get(id=userid)
    return render(request,'checkout.html',{'userdetails':userdetails,'productdetails':productslist,'orderid':orderid,'total':ttotal,'advanceamount':advance_amount,'balanceamount':balance_amount})


"""
        
"""
def singleproductorder(request):
    userid = request.session['userid']
    orderlist = orderlist_details.objects.order_by('orderid').last()
    if orderlist is None:
        orderid = 1
    else:
        orderid = orderlist.orderid + 1
    productid = request.POST['productid']
    product_id = ProductDetails.objects.get(id=productid)
    productslist = ProductDetails.objects.filter(id=productid)
    for product in productslist:
        price = product.prodprice
    quantity = request.POST['quant']
    if int(quantity) >= 1:
        subtotal = int(quantity) * int(price)
        item = orderlist_details.objects.create(orderid=orderid, userid=userid, prod_id=product_id, quantity=quantity,
                                            price=price, subtotal=subtotal)
        item.save();
        advance_amount = (subtotal * 10) // 100
        balance_amount = subtotal - advance_amount
        userdetails = User.objects.get(id=userid)
        return render(request, 'checkout.html',{'userdetails': userdetails, 'product': productslist, 'orderid': orderid, 'total': subtotal,'advanceamount': advance_amount, 'balanceamount': balance_amount})
    else:
        messages.error(request, 'Enter a valid quantity!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


"""
    GETTING DELIVERING DETAILS AND FINAL CONFIRMATION OF ORDER
"""
def confirmation(request):
    userid = request.session['userid']
    if request.method == 'POST':
        delivering_date = request.POST['delivering_date']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        address = address1 + " , " + address2
        town = request.POST['town']
        postcode = request.POST['pincode']
        phone = request.POST['phone_no']
        password = request.POST['password']
        order_notes = request.POST['order_notes']
        orderid = request.POST['orderid']
        total_price = request.POST['totalprice']
        advance_amount = request.POST['advanceamount']
        balanace_amount = request.POST['balanceamount']
        count = request.POST['count']
        print("..................",count)
        username = User.objects.get(id=userid)
        #order_id = orderlist_details.objects.get(orderid=orderid)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print("Success")
            item = Final_Order_Table.objects.create(orderid=orderid,userid=userid,deliver_date=delivering_date,address=address,town=town,postcode=postcode,phone=phone,order_notes=order_notes,total_price=total_price,advance_amount=advance_amount,balance_amount=balanace_amount,status="Ordered",no_of_products=count)
            item.save();
            return render(request, 'confirmation-page.html')
        else:
            messages.error(request, 'Invalid Password')
            return redirect('confirmation')
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



"""
    CANCEL ORDER 
"""
def cancelorder(request,orderid):
    print(".................orderid",orderid)
    ordered_products = orderlist_details.objects.filter(orderid=orderid)
    ordered_products.delete()
    print("success")
    return redirect('shoppingcart')


"""
    VIEWING SINGLE PRODUCT DETAILS
"""
def productdetails(request,prodid,userid):
    product = ProductDetails.objects.filter(id=prodid)
    cartbutton(request,prodid,userid)
    data = {}
    productid = ProductDetails.objects.get(id=prodid)
    if cart_items.objects.filter(userid=userid, prod_id=productid).exists():
        val = 1
        data['val'] = 1
    else:
        val = 0
        data['val'] = 0
    if wishlist_items.objects.filter(userid=userid, prod_id=productid).exists():
        wishcart = 1
    else:
        wishcart = 0
    return render(request,'productdetails.html',{'product':product,'data':val,'wishlist':wishcart})


"""
        VIEWING WISHLIST
"""
def view_wishlist(request):
    wishlist_counts(request)
    wishlist_count = request.session['count_wishlist']
    print("..............",wishlist_count)
    userid = request.session['userid']
    items = wishlist_items.objects.filter(userid=userid).order_by('-id')
    if items is not None:
        for product in items:
            productid = product.prod_id.id
            if productid is not None:
                return render(request, "wishlist.html", {'products': items,'wishlist_count': wishlist_count})
            else:
                return render(request, "wishlist.html", {'products': items, 'wishlist_count': wishlist_count})
    else:
        return render(request, "wishlist.html", {'products': items})
    return render(request, "wishlist.html", {'products': items})




"""
        ADDING ITEMS TO WISHLIST
"""
def addwishlist(request, prodid, userid):
    productid = ProductDetails.objects.get(id=prodid)
    if wishlist_items.objects.filter(userid=userid, prod_id=productid).exists():
        print("Item already added")
    else:
        items = wishlist_items.objects.create(userid=userid, prod_id=productid)
        items.save();
    wishlist_counts(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return redirect('users_home')


"""DELETE FROM WISHLIST"""

def delete_wishlist(request, prodid):
    productid =prodid
    userid = request.session['userid']
    item = wishlist_items.objects.filter(userid=userid,prod_id=productid)
    item.delete()
    wishlist_counts(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return redirect('view_wishlist')

"""
    LOG OUT SESSION 
"""

def logout(request):
    auth.logout(request)
    return redirect('/')
