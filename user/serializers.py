#Using default User Model
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerialiser(serializers.ModelSerializer):
    '''serializer for User Model'''
    class Meta:
        model = User
        fields = '__all__'