from django.shortcuts import render
from .models import Inventory,Sell
from .forms import Inventory_form
from django.views.generic import ListView

# Create your views here.


def create_inventory(request):                                          #adding inventory
    if request.method == 'POST':
        form = Inventory_form(request.POST)
        if form.is_valid():
            form.save()
            try:
                queryset = Inventory.objects.latest('inventory_id')  #qs is just a variable, latest id
                inv_id = queryset.inventory_id +1
            
                
            except:
                inv_id = 1                                   # exception for inventory 


    else:
        form = Inventory_form(initial={'status': 'Stock'})  
        try:
            queryset = Inventory.objects.latest('inventory_id')  
            inv_id = queryset.inventory_id +1
        
            
        except:
            inv_id = 1                   

    return render(request, 'inventory.html', { 'inv_id': inv_id, 'form': form })


class Inventory_List(ListView):                                         #inventory_list
    model=Inventory
    template_name='inventory_list.html'
    context_object_name='inventory_list'


def Sold_list(request):                                          #sold_list
    qs = Inventory.objects.all().filter(status='Sold')
    return render(request, 'sold_list.html', {'qs': qs })

    
    



