from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserMy

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMy
        fields = '__all__'

