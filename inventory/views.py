from django.shortcuts import render
from .models import Inventory
from .forms import Inventory_form

# Create your views here.


def create_inventory(request):
    if request.method == 'POST':
        form = Inventory_form(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = Inventory_form(initial={'operation': 'stock'})
        queryset = Inventory.objects.latest('inventory_id')
        inv_id = queryset.inventory_id +1

    return render(request, 'inventory.html', {'form': form, 'inv_id': inv_id})
