from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsersSerializer
from .models import CustomUser
import json

# Create your views here.

class Usersview(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = CustomUser.objects.all()