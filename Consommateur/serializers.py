from rest_framework import serializers
from Consommateur.models import Consommateur


class ConsommateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consommateur
        fields = '__all__'
