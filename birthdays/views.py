from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Birthday
from .serializers import BirthdaySerializer

@api_view(['GET'])
def list_birthdays(request):
    birthdays = Birthday.objects.all()
    serializer = BirthdaySerializer(birthdays, many=True)
    return Response(serializer.data)
