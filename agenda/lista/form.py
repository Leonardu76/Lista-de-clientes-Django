from django.forms import ModelForm
from .models import Usuarios
from django import forms
import requests



response = requests.get('http://gerador-nomes.herokuapp.com/nome/aleatorio')
todos = response.json()
name = todos[0]
sobrename = todos[1]  



class UsuariosForm(ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class":"for", "value":name}))
    sobrenome = forms.CharField(widget=forms.TextInput(attrs={"class":"for", "value":sobrename}))
    idade = forms.CharField(widget=forms.TextInput(attrs={"class":"for", "placeholder":"Digite a idade"}))
    data_nascimento = forms.CharField(widget=forms.TextInput(attrs={"class":"for","type":"date", "placeholder":"Digite a data de nascimento"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"for", "placeholder":"digite o email"}))
    apelido = forms.CharField(widget=forms.TextInput(attrs={"class":"for", "placeholder":"Digite o apelido"}))
    observacao = forms.CharField(widget=forms.Textarea(attrs={"class":"texar", "rows":"5"}))


    class Meta:
        model = Usuarios
        fields = ['nome', 'sobrenome', 'idade', 'data_nascimento', 'email', 'apelido', 'observacao']