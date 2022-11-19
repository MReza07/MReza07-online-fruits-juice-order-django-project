from django.contrib import admin
from .models import CartItem


@admin.register(CartItem)
class CartItemtModelAdmin(admin.ModelAdmin):
    list_display = ['cid', 'uid', 'pid', 'qty', 'price','deliveryCharge', 'ordered']


