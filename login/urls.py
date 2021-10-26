from django.urls import path

from .import views

urlpatterns=[
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('users_home',views.users_home,name="users_home"),
    path('logout',views.logout,name="logout")
]