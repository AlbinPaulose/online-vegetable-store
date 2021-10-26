from django.contrib import admin
from .models import*

# Register your models here.
#class FinalOrderAdmin(admin.ModelAdmin):
    #list_display = ['id','orderid']
admin.site.register(orderlist_details)
admin.site.register(Final_Order_Table)
