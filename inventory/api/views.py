from rest_framework import viewsets

from inventory.models import Inventory
from inventory.api.serializers import InventorySerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
