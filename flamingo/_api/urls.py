from django.urls import path
from .shop.item import add_item, get_items

urlpatterns = [
    path('shop/items/add', add_item),
    path('shop/items/all', get_items),
]