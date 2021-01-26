from django.shortcuts import render

# Create your views here.


def create_buy(request):
    return render(request, 'buy.html')
