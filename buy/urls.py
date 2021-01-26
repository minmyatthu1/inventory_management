from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_buy, name='create_buy'),
    # path('list', )
]
