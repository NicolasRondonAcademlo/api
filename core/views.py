from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer

@csrf_exempt
def user_create(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(
           users, many=True
        )
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(
            data=data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201 )
        return JsonResponse(serializer.errors, status=400)