from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import Users


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = Users
        fields = ('username', 'password')


class RegistrationUser(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = Users
        fields = ('username', 'password1', 'password2')

a = 1, 2, 3
print(a)