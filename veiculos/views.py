from django.shortcuts import render
from .models import Veiculo

def veiculo_list(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/veiculo_list.html', {'veiculos': veiculos})