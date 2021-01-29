from django.urls import path

from inventory.apps import InventoryConfig
from inventory.api.views import InventoryViewSet

app_name = InventoryConfig.name

urlpatterns = [
    path('inventory', InventoryViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='inventory-view'),
    path('inventory/<id>', InventoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='inventory-detailview'),
]
