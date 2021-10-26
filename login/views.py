from django.shortcuts import render,redirect
from django.contrib import messages
from  django.contrib.auth.models import  User, auth
from home_main.models  import ProductDetails
from customer_activity.models import cart_items,wishlist_items
from django.http import HttpResponse

# Create your views here.

'''customers login checking'''
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            request.session['userid'] = user.id
            return redirect('users_home')
        else:
            messages.error(request, 'Invalid Credentails')
            return redirect('login')
    else:
        return render(request,'login.html')


'''Sign Up code for  new  customer i.e registering'''
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email id is Already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password2, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                messages.success(request,'Account Created Successfully!!! Login to explore ')
                return redirect('login')

        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
    else:
        return render(request,'userregistration.html')


"""
    COUNTING NO. OF ITEMS IN CART
"""
def cart_items_counts(request):
    cartitems_count = 0
    userid = request.session['userid']
    items = cart_items.objects.filter(userid=userid).order_by('-id')
    if items is not None:
        for i in items:
            cartitems_count += 1
    request.session['count_cartitems'] = cartitems_count



"""
    COUNTING NO. OF ITEMS IN WISHLIST
"""
def wishlist_counts(request):
    wishlist_count = 0
    userid = request.session['userid']
    items = wishlist_items.objects.filter(userid=userid)
    if items is not None:
        for i in items:
            wishlist_count += 1
    request.session['count_wishlist'] = wishlist_count


'''Customer home page '''
def users_home(request):
    products = ProductDetails.objects.all()

    userid = request.session['userid']
    items = cart_items.objects.filter(userid=userid)
    for product in items:
        print(".................",product.prod_id.id)


    cart_items_counts(request)
    wishlist_counts(request)
    cartitems_count = request.session['count_cartitems']
    wishlist_count = request.session['count_wishlist']
    latestproducts = ProductDetails.objects.order_by('-addondate')[:5] #code for getting newly added 5 products
    return render(request, 'home.html',{'products': products,'recentproducts':latestproducts,'cartitems_count':cartitems_count,'wishlist_count':wishlist_count,'inCart':items})


'''Customer logout session'''
def logout(request):
    auth.logout(request)
    return redirect('/')


