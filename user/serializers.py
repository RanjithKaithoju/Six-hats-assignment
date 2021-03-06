#Using default User Model
from django.contrib.auth.models import User
from rest_framework import fields, serializers
from rest_framework.exceptions import ValidationError

class UserSerialiser(serializers.ModelSerializer):
    '''serializer for User Model'''
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['id','is_superuser','email','date_joined','username']
        extra_kwargs = {'date_joined':{'required':False}}

        #Simple Inbuilt Validator
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username']
            )
        ]