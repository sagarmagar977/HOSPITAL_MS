from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import mixins
from .serializers import *
from .models import user
from core.permisson import CustomModelPermission


class groupView(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset=Group.objects.all()
    serializer_class=groupserializers
    permission_classes=[CustomModelPermission]


from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email=request.data.get('email')
    password=request.data.get('password')
    user=authenticate(username=email,password=password)
    if user is None:
        return Response("INVALID EMAIL OR PASSWORD !!!")
    else:
        token,_=Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([AllowAny])

def register(request):
    password=request.data.get('password')
    request.data['password']=make_password(password)
    serializers=userserializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response('congrats ! user created !')
    else : 
        return Response(serializers.errors)


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from core.permisson import CustomModelPermission
class AlluserView(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset=user.objects.all()
    serializer_class=userListSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['email']
    search_fields=['email']
    permission_classes=[CustomModelPermission]
# Create your views here.
