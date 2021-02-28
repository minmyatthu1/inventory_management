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


# class All_Inventory_List(ListView):                                        
#     model=Inventory
#     template_name='all_inventory.html'
#     context_object_name='all_inventory'
#     ordering = ['-inventory_id']


def All_Inventory_List(request):                                           #all inventory_list
    all_inven_list = Inventory.objects.all().order_by('inventory_id')
    return render(request, 'all_inventory.html', {'all_inven_list': all_inven_list })


def Inventory_List(request):                                          #inventory_list
    inven_list = Inventory.objects.all().filter(status='Stock').order_by('inventory_id')
    return render(request, 'inventory_list.html', {'inven_list': inven_list })


def Sold_list(request):                                          #sold_list
    qs = Inventory.objects.all().filter(status='Sold')
    return render(request, 'sold_list.html', {'qs': qs })

    
    



