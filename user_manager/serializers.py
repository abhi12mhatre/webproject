# serializers.py
from rest_framework import serializers

from .models import UserProfile, UserExtra


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtra
        fields = '__all__'
