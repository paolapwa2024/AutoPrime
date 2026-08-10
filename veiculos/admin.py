from django.contrib import admin
from .models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'placa', 'cor', 'proprietario', 'is_active')
    search_fields = ('marca', 'modelo', 'placa', 'proprietario')
    list_filter = ('marca', 'is_active', 'ano')