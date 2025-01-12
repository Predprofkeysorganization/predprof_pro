from django.shortcuts import *
from users.forms import UserLoginForm
from django.urls import reverse
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('http://127.0.0.1:8000/registration')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'auth.html', context)
