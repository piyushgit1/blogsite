from django.views import View
from django.shortcuts import render
from .serializer import UserLoginSerializer
from .models import UserLogin
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

class UserLoginViewset(viewsets.ModelViewSet):
      queryset = UserLogin.objects.all()
      serializer_class = UserLoginSerializer







