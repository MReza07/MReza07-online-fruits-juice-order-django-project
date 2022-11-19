from django.urls import path, include
from . import views

urlpatterns = [
    path('trending/', views.trending, name='trending'),
    path('filterByCategory/<category>/', views.filterByCategory, name='filterByCategory'),
    path('allfruits/<category>/', views.allfruitsByCategory, name='allfruitsByCategory'),
    path('product/<int:pid>/', views.get_product, name='get_product'),
    path('product/search/', views.search_product, name='search'),
    path('review_rating/<int:pid>', views.review_show, name='review_rating'),


]
