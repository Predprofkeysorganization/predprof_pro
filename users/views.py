from django.shortcuts import *
from users.forms import UserLoginForm, RegistrationUser
from django.urls import reverse
from django.contrib import auth
from users.models import Users


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('http://127.0.0.1:8000/main')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'auth.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationUser(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/main')
    else:
        form = RegistrationUser()
    return render(request, 'registration_admin.html', context={'form': form})
