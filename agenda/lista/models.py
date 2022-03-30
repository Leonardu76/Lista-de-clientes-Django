from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    idade = models.IntegerField()
    data_nascimento = models.DateField(max_length=10,)
    email = models.EmailField(max_length=255,)
    apelido = models.CharField(max_length=13, null=True, blank=True)
    observacao = models.TextField(max_length=150, null=True, blank=True, verbose_name='Observação')

   
