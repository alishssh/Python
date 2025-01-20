from django.contrib import admin
from .models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email')



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')
    search_fields = ('customer__name',)
    list_filter = ('status', 'created_at')
    filter_horizontal = ('product',)  # For Many-to-Many fields
