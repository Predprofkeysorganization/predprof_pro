from django.shortcuts import render, HttpResponseRedirect
from user.models import Inventory, Application
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, 'base.html', context={'inventory': Inventory.objects.all()})


def main1(request):
    print(request.POST.get('name', 'n'))
    return render(request, 'main.html', context={'inventory': Inventory.objects.all()})


def authorization(request):
    return render(request, 'auth.html')


def authorization1(request):
    print(request.GET.get('application_1', '1'))
    print(request.GET.get('application_2', '1'))
    app = Application(id_application=request.GET.get('application_1', '1'), status_application='необработана')
    app.save()
    print(Application.objects.all())
    return render(request, 'application.html')
    # return HttpResponseRedirect(reverse('index'))


# def registration(request):
#     return render(request, 'registration_admin.html')
