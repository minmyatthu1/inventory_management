from django.db.models.signals import post_save
from django.shortcuts import render
from .forms import Sell_form
from django.views.generic import ListView
from inventory.models import Sell, Inventory

# Create your views here.

def create_sell(request):
    if request.method == 'POST':
        form = Sell_form(request.POST)
        if form.is_valid():
            print (form.cleaned_data['inventory'])

            p= form.cleaned_data['inventory']         #take field         
            get_inv_id = p.inventory_id               #assign inventory id 

            def update_inventory(sender, instance, **kwargs):           #signals
                print("updated")
                b = Inventory.objects.get(pk=get_inv_id)
                b.status = "Sold"
                b.save()                # update inventory status when signal come
            post_save.connect(update_inventory, sender=Sell)
            form.save()

    else:
        # form = Sell_form(initial={'sell_date' : date.today() })
        form = Sell_form()

    return render(request, 'sell.html', {'form': form})



