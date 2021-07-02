from rest_framework import serializers

from .models import Birthday

class BirthdaySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=True)
    
    class Meta:
        model = Birthday
        fields = ('name', 'birth_date')