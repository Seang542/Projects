from django.contrib import admin
from productsapp.models import Product

class ManageProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'isTreanding')
    list_editable = ['price', 'stock', 'isTreanding']
    list_per_page = 5
    search_fields = ['name']
    list_filter = ['isTreanding', 'price']


# Register your models here.
admin.site.register(Product,ManageProduct)

