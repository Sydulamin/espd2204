from django.contrib import admin
from .models import *


# Register your models here.


class Product_List(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(Category)
admin.site.register(Product, Product_List)
