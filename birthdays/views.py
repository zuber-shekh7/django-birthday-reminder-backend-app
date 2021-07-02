from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Birthday
from .serializers import BirthdaySerializer

@api_view(['POST'])
def create_birthday(request):
    serializer = BirthdaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_birthdays(request):
    birthdays = Birthday.objects.all()
    serializer = BirthdaySerializer(birthdays, many=True)
    return Response(serializer.data)
