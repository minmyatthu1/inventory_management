from django.urls import path

from .apps import InventoryConfig
from . import views

app_name = InventoryConfig.name

urlpatterns = [
    path('', views.create_inventory, name='inventory'),
]
