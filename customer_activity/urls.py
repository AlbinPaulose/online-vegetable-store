from django.urls import path,re_path

from .import views

urlpatterns = [
    path('shoppingcart',views.shoppingcart,name="shoppingcart"),
    path('logout',views.logout,name="logout"),
    path('addcart/<int:prodid>/<int:userid>/', views.addcart,name="addcart"),
    path('deletecart/<int:prodid>/',views.deletecart,name="deletecart"),
    path('updatequantity',views.updatequantity,name="updatequantity"),
    path('placeorder',views.placeorder,name="placeorder"),
    path('orderproducts',views.orderproducts,name='orderproducts'),
    path('confirmation',views.confirmation,name='confirmation'),
    path('productdetails/<int:prodid>/<int:userid>/',views.productdetails,name='productdetails'),
    path('singleproductorder',views.singleproductorder,name='singleproductorder'),
    path('view_wishlist',views.view_wishlist,name='view_wishlist'),
    path('addwishlist/<int:prodid>/<int:userid>/', views.addwishlist, name='addwishlist'),
    path('delete_wishlist/<int:prodid>/',views.delete_wishlist,name="delete_wishlist"),
    path('cancelorder/<int:orderid>/',views.cancelorder,name="cancelorder"),
    path('my_orders',views.my_orders,name="my_orders"),
    path('view_order_details/<int:orderid>/<int:total_price>/<int:adv_amount>/<int:bal_amount>/<str:status>/',views.view_order_details,name="view_order_details"),
    path('cancel_order/<int:orderid>/',views.cancel_order,name="cancel_order"),
    #re_path(r'^(?P<prodid>\d{1,5})/(?P<prodname>\w+)/(?P<prodpiceunit>\w+)/(?P<prodprice>\w+)/$',views.addcart,name="addcart"),
]