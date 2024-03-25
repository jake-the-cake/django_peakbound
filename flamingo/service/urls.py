from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('items/', views.item_list),
    # path('items/add/', views.add_item),
    # path('items/<str:id>/', views.view_item),
    # path('orders/', views.view_item),
    # path('orders/cart/', views.view_cart),
]