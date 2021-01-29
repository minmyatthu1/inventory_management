from django.urls import path

from .apps import BuyConfig
from . import views

app_name = BuyConfig.name

urlpatterns = [
    path('', views.create_buy, name='create_buy'),
    # path('list', )
]
