from rest_framework import serializers
from .models import *

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'
        extra_kwargs = {
            'id' : {'read_only':  True},
        }

class usersidSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['first_name','last_name','age']
        