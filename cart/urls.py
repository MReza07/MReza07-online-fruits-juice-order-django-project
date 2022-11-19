from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cartview, name='cartview'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('removeitem/<int:id>/', views.removeitem, name='removeitem'),



]
