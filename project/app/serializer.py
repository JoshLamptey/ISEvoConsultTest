from rest_framework import serializers
from .models import Client
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = 'all'