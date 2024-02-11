from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
from rest_framework.decorators import api_view

from rest_framework import status

from projectuser.models import User


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh'
    ]
    return Response(routes)

class MyTokenObtainPairSerializers(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        if user.is_active:
            token = super().get_token(user)
            # add custom claims to the token payload
            token['username'] = user.username
            # token[]
            return token
        else:
            return Response('username is  jhuyjgbjbhj not valid')


class MyTokenObtainPairview(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializers


@api_view(['POST'])
def sign_up(request):
    print("request came Here")
    firstname = request.data['firstname']
    lastname = request.data['lastname']
    phoneno = request.data['phoneno']
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']

     # Use UserManager to create a new user instance
    if User.objects.filter(username = username):
        return Response('username not available', status=status.HTTP_401_UNAUTHORIZED)
    if User.objects.filter(email = email):
        return Response("Already register with this email",status=status.HTTP_406_NOT_ACCEPTABLE)
    user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,phoneno=phoneno,password=password)
    user.save()
    user__ = User.objects.all()
    
    
    return Response({'status':'success'})
