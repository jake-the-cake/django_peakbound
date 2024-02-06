from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('items/', views.item_list),
    path('items/add/', views.add_item),
    # path('items/edit/', views.edit_item),
]