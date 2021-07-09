from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegistrationSerializer


@api_view(['POST'])
def signup(request):
    serializer = UserRegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        instance = serializer.save()
        data['response'] = 'User Registered Successfully'
        data['email'] = instance.email
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
