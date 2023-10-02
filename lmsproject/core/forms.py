from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno

class AlunoRegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Aluno
        fields = ['username', 'email', 'password1', 'password2']
