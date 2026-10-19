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

    def clean_email(self):
        email = self.cleaned_data['email'].strip()

        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado. Entre na sua conta.'
            )

        return email
