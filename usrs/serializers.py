from rest_framework import serializers
from .models import CustomUser

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'username', 'first_name','last_name','email','date_joined','is_active','is_staff','is_superuser','last_login')