from django.db import models

class Veiculo(models.Model):
    marca = models.CharField(max_length=50, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    ano = models.IntegerField(verbose_name='Ano')
    placa = models.CharField(max_length=8, unique=True, verbose_name='Placa')
    cor = models.CharField(max_length=30, verbose_name='Cor')
    proprietario = models.CharField(max_length=100, verbose_name='Proprietário')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['marca', 'modelo']
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'