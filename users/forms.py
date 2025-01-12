from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import Users


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = Users
        field = ('username', 'password')
