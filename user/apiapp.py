from user.models import Application
from rest_framework import viewsets, permissions
from user.serializer import Application_table_serializers


class Application_ser(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Application_table_serializers