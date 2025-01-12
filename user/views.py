from django.shortcuts import render
from user.models import Inventory


# Create your views here.


def index(request):
    return render(request, 'base.html')


def main1(request):
    return render(request, 'main.html', context={'inventory': Inventory.objects.all()})


def authorization(request):
    return render(request, 'auth.html')


def registration(request):
    return render(request, 'templates_registration/registration_admin.html')
