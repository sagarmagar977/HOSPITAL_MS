from rest_framework import serializers
from .models import *

class Patientinfoserializers(serializers.ModelSerializer):
    class Meta:
        model=PatientInfo
        fields="__all__"
class medicalrecordserializers(serializers.ModelSerializer):
    class Meta:
        model=MedicalRecord
        fields="__all__"

class Prescriptionserializers(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields="__all__"