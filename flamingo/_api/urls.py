from django.urls import path
from .shop.item import add_item, get_items, edit_item, delete_item
from .shop.order import add_order

urlpatterns = [
    path('shop/items/add', add_item),
    path('shop/orders/add', add_order),
    path('shop/items/all', get_items),
    path('shop/items/<str:id>/edit', edit_item),
    path('shop/items/<str:id>/delete', delete_item),
]