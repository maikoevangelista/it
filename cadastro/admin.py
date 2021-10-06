from django.contrib import admin
from .models import Cadastro

@admin.register(Cadastro)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome','email', 'telefone', 'cpf', 'Logradouro','Número','Bairro','Complemento','cep')