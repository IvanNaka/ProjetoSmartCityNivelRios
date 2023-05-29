
from django import forms
from django.contrib.auth.models import User
# from core.models import UsuarioLogin


class SignUpForm(forms.Form):
    # username = forms.CharField(label='Usuário', max_length=100)
    primeiro_nome = forms.CharField(label='Primeiro nome', max_length=100)
    ultimo_nome = forms.CharField(label='Último nome', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    email = forms.EmailField(label='E-mail')
    celular = forms.CharField(label='Celular')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('As senhas não coincidem.')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


ESCOLHAS_RIOS =(
    ("1", "Rio Piraquara"),
    ("2", "Rio Barigui"),
    ("3", "Rio Atuba "),
)


class RiosForm(forms.Form):
    rios_field = forms.MultipleChoiceField(choices=ESCOLHAS_RIOS)
