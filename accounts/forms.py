from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class CadastroForm(UserCreationForm):
    nome = forms.CharField(
        label='Nome',
        max_length=100
    )

    sobrenome = forms.CharField(
        label='Sobrenome',
        max_length=100
    )

    email = forms.EmailField(
        label='E-mail'
    )

    class Meta:
        model = Usuario
        fields = [
            'nome',
            'sobrenome',
            'username',
            'email',
        ]
        labels = {
            'username': 'Nome de usuário',
        }
