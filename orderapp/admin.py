from django.contrib import admin
from .models import order


@admin.register(order)
class orderModelAdmin(admin.ModelAdmin):
    list_display = ['oid', 'cartitem', 'first_name', 'last_name', 'email', 'addr', 'town', 'zipcode', 'phone',
                    'comment', 'status']
