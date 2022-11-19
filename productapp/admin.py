from django.contrib import admin
from .models import product, review_rating


# Register your models here.
@admin.register(product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['pid', 'title', 'price', 'weight', 'category', 'delivery', 'in_stock', 'image']


@admin.register(review_rating)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['uid', 'pid', 'title', 'review', 'rate', 'status', 'created_date', 'update_date']
