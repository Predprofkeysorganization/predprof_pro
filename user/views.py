from django.http import HttpResponse
from django import forms
from django.shortcuts import render, HttpResponseRedirect
from user.models import Inventory, Application, ApplicationRepair
from users.forms import ApplicationForm
from django.urls import reverse


# Create your views here.


def index(request):
    return render(request, 'main.html', context={'inventory': Inventory.objects.all()})


# def main1(request):
#     return render(request, 'main1.html', context={'inventory': Inventory.objects.all()})
#
#
# def authorization(request):
#     return render(request, 'auth.html')


def application(request):
    if request.method == 'POST':

        dict_obj_1 = dict(request.POST)
        get_object = dict_obj_1.get('application_2')
        text_info = ''.join(get_object) if ''.join(get_object) != '' else 'Сообщение отсутствует'
        app = Application(name_application=request.user.username, information=text_info,
                            status_application='необработана')
        app.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'application.html',
                  context={'table': list(Application.objects.filter(name_application=request.user.username))})


def authorization_repair(request):
    if request.method == 'POST':
        dict_obj_1 = dict(request.POST)
        get_object_1 = dict_obj_1.get('application_4')
        if get_object_1[0]:
            app = ApplicationRepair(name=request.user.username, repair_info=''.join(get_object_1))
            app.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'application_remont.html',
                  context={'table': list(ApplicationRepair.objects.filter(name=request.user.username)),
                           'form': ApplicationForm()})
    # return render(request, 'application_remont.html')

# def registration(request):
#     return render(request, 'registration.html')

