from django.contrib import admin
from .models import *

admin.site.register(PatientInfo)
admin.site.register(MedicalRecord)
admin.site.register(Prescription)
# Register your models here.
