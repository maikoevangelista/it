from django.db import models
class Cadastro(models.Model):
    nome = models.CharField('Nome ', max_length=250)
    email = models.CharField('E-mail', max_length=250, null=True,blank=True)
    telefone = models.CharField('Núm. telefone', max_length=250)
    cpf = models.CharField('Informe seu CPF ', max_length=250)
    Logradouro = models.CharField('Logradouro', max_length=250)
    Número = models.CharField('Número', max_length=250)
    Bairro = models.CharField('Bairro', max_length=250)
    Complemento = models.CharField('Complemento', max_length=250)
    cep = models.CharField('CEP', max_length=250)

    def __str__(self):
        return str(self.nome)
        
    class Meta:
        verbose_name = 'cadastros'
        verbose_name_plural = 'cadastro'