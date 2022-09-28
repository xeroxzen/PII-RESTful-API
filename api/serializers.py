from rest_framework import serializers
from .models import Pii

class PiiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pii
        fields = '__all__'