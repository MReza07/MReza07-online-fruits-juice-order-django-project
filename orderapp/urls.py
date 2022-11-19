from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('myorder/<int:id>/', views.myorder, name='myorder'),
    path('myorder/cancel/<int:oid>/', views.cancel, name='cancelmyorder'),
    # REST API
    path('get_orders/', views.OrderApiView.as_view(), name='get_orders'),
    path('get_orders/<int:oid>/', views.OrderAPIDetail.as_view(), name='get_orders'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
