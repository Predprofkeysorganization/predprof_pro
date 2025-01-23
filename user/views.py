from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from user.models import Inventory, Application, ApplicationRepair
from django.urls import reverse


# Create your views here.


def index(request):
    return render(request, 'base.html', context={'inventory': Inventory.objects.all()})


def main1(request):
    return render(request, 'main.html', context={'inventory': Inventory.objects.all()})


def authorization(request):
    return render(request, 'auth.html')


def authorization1(request):
    if request.method == 'POST':
        dict_obj_1 = dict(request.POST)
        get_object = dict_obj_1.get('application_1', False)
        if get_object[0]:
            app = Application(name_application=''.join(get_object), status_application='необработана')
            app.save()
            return HttpResponseRedirect(reverse('main'))
    return render(request, 'application.html', context={'table': Application.objects.all()})


def authorization2(request):
    if request.method == 'POST':
        dict_obj_1 = dict(request.POST)
        get_object = dict_obj_1.get('application_3', False)
        get_object_1 = dict_obj_1.get('application_4', False)
        if get_object[0]:
            app = ApplicationRepair(name=''.join(get_object), repair_info=''.join(get_object_1))
            app.save()
            return HttpResponseRedirect(reverse('main'))
    return render(request, 'application_remont.html', context={'table': ApplicationRepair.objects.all()})
    # return render(request, 'application_remont.html')

# def registration(request):
#     return render(request, 'registration_admin.html')
