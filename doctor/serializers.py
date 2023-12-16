from rest_framework import serializers
from .models import *

class doctorinfoserializers(serializers.ModelSerializer):
    class Meta:
        model=DoctorInfo
        fields="__all__"
