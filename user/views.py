from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerialiser
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.
@api_view(['GET','POST'])
def user_list(request):
    '''Lists and create Users'''
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerialiser(users,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = UserSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        