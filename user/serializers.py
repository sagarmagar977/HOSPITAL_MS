from rest_framework import serializers

from django.contrib.auth.models import Group
from .models import user

class userserializers(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['id','email','password','groups']
class groupserializers(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields=['id','name']

class userListSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=["id","username",'email',"groups"]