from django.shortcuts import render
from .forms import Sell_form

# Create your views here.

def create_sell(request):
    if request.method == 'POST':
        form = Sell_form(request.POST)
        if form.is_valid():
            form.save()

    else:
        # form = Sell_form(initial={'sell_date': ''})
        form = Sell_form()

    return render(request, 'sell.html', {'form': form})

