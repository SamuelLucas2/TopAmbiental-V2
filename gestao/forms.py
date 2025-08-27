from django import forms
from .models import Cliente, Documento
from django.contrib.auth.models import User

class AdminLoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ClientLoginForm(forms.Form):
    cnpj = forms.CharField(label="CNPJ", widget=forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ClienteForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Deixe em branco para não alterar'}),
        required=False,
        help_text="Deixe em branco para não alterar."
    )
    class Meta:
        model = Cliente
        fields = ['nome_empresa', 'cnpj', 'senha']
        widgets = {
            'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['titulo', 'arquivo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        help_texts = {'username': 'Obrigatório. Use um nome de usuário único.'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }