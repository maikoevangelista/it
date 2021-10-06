from django.shortcuts import render, redirect
from .models import Cadastro
from .forms import CadastroForm
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
def Cadastro(request):
    Cadastro = Cadastro.objects.all(JWTAuthentication)
    refresh = RefreshToken.for_user(user)

    
    if request.method=='POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('mensagem')
            
    else:
        form = CadastroForm()
        
        dados = {
             "form": form,
    }

    
    
    return render(request, "site.html", dados)
    'refresh': str(refresh),
        'access': str(refresh.access_token),


def mensagem(request):
    return render(request, "mensagem.html")
    
