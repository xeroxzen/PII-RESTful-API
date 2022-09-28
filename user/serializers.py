from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models  import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', 'last_login', 'date_joined')