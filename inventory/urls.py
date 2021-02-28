from django.urls import path
from . import views
from .views import Inventory_List,All_Inventory_List

urlpatterns = [
    path('', views.create_inventory, name='inventory'),
    path('allinventorylist/',views.All_Inventory_List, name='all_inventory_list'),
    path('inventorylist/', views.Inventory_List, name='inventory_list' ),
    path('sold_list/', views.Sold_list, name='sold_list' )

]
