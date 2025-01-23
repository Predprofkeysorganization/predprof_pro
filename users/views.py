from django.shortcuts import *
from users.forms import UserLoginForm, RegistrationUser
from django.urls import reverse
from django.contrib import auth
from user.models import Application
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
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'auth.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationUser(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = RegistrationUser()
    return render(request, 'registration_admin.html', context={'form': form, 'table': Application.objects.all()})
