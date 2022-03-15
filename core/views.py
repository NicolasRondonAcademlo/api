from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import  Response
from  rest_framework import status
from .serializers import CreateUserSerializer, UserSerializer
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def user_create(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(
           users, many=True
        )
        # return JsonResponse(serializer.data, safe=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = CreateUserSerializer(
            data=request.data
        )
        if serializer.is_valid():
            user = serializer.save()
            user = User.objects.get(pk=user.id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)