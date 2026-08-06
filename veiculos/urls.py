from django.urls import path
from . import views

urlpatterns = [
    path('', views.veiculo_list, name='veiculo_list'),
]