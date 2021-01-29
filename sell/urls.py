from django.urls import path

from .apps import SellConfig
from . import views


app_name = SellConfig.name

urlpatterns = [
    path('', views.create_sell, name='sell')
]
