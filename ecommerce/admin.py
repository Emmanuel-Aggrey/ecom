from django.contrib import admin
from .models import Product,Category,Sub_Category
from orders.models import OrderItem
# Register your models here
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','name','price','is_available']

    list_filter = ['category','is_available']




admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product,ProductAdmin)
