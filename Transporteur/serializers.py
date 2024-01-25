from rest_framework import serializers
from Transporteur.models import TransporteurInfo


class TransporteurInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransporteurInfo
        fields = '__all__'
