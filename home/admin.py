from re import search
from django.contrib import admin
from .models import Product,Buy,Users
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductName','price']
    search_fields = ['ProductCode']
    list_filter = ['ProductName','price']

admin.site.register(Product,ProductAdmin)
admin.site.register(Buy)
admin.site.register(Users)