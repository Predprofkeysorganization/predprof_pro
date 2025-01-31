from user.serializer import PlanSerializer
from django.urls import path
urlpatterns = [
    path('apikey/', PlanSerializer.as_view(), name='apiplan')
]
