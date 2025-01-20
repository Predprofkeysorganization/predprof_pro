from rest_framework import serializers
from user.models import Application


class Application_table_serializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'