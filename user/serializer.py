from rest_framework import serializers
from rest_framework.generics import ListAPIView
from user.models import Plan


class SerializerPlan(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'name', 'price', 'count', 'provider')


class PlanSerializer(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = SerializerPlan