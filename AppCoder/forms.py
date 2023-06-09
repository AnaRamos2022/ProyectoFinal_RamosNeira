from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        #mensajes de ayuda
        help_texts = {k:"" for k in fields}
