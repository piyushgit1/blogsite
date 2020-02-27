from rest_framework import serializers
# TODO: dont use .
from .models import UserLogin, Registration


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['id', 'Username', 'Password']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'Username', 'Password', 'Email']
