from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerialiser
from rest_framework.response import Response
from rest_framework import  serializers, status
from rest_framework import pagination

# Create your views here.
@api_view(['GET','POST'])
def user_list(request):
    '''Lists and create Users'''
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerialiser(users,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class StandardResultSetPagination(pagination.PageNumberPagination):
    '''Pagination Configuration'''
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 1000

@api_view(['GET'])
def users(request):
    '''Gives data with pagination'''
    #Taking newest first
    users = User.objects.all().order_by('-id')
    if len(users) > 0:
        paginator  = StandardResultSetPagination()
        result_page = paginator.paginate_queryset(users,request)
        serializer = UserSerialiser(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)
    return Response({"msg":"End of the page.."},status=status.HTTP_204_NO_CONTENT)