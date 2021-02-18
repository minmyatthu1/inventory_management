from django.urls import path
from . import views
from .views import Inventory_List

urlpatterns = [
    path('', views.create_inventory, name='inventory'),
    path('inventorylist/',Inventory_List.as_view(), name='inventory_list'),
    path('sold_list/', views.Sold_list, name='sold_list' )

]
