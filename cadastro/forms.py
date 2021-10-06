from django.forms import ModelForm
from .models import *

class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'