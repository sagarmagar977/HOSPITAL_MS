from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework import viewsets
from rest_framework import mixins

class patientInfoView(viewsets.ModelViewSet):
    queryset=PatientInfo.objects.all()
    serializer_class=Patientinfoserializers

class medicalrecordView(viewsets.ModelViewSet):
      queryset=MedicalRecord.objects.all()
      serializer_class=medicalrecordserializers

class prescriptionview(viewsets.ModelViewSet):
     queryset=Prescription.objects.all()
     serializer_class=Prescriptionserializers

# Create your views here.
