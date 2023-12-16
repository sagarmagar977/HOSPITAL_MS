from django.db import models
from doctor.models import DoctorInfo

# Create your models here.


class PatientInfo(models.Model):
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    DOB=models.DateField(null=False)
    gender_choice=[('male','male'),('female','female')]
    gender=models.CharField(choices=gender_choice,max_length=100)
    address=models.CharField(max_length=300)
    phone_number=models.IntegerField(default=None,null=True,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    def __str__(self):
        return self.f_name

class MedicalRecord(models.Model):
    patient=models.ForeignKey(PatientInfo,on_delete=models.CASCADE)
    doctor=models.ForeignKey(DoctorInfo,on_delete=models.PROTECT)
    admision_date=models.DateTimeField(auto_now_add=True)
    discharge_date=models.DateTimeField(null=True)
    diagnosis=models.CharField(max_length=1000)
    treatment=models.CharField(max_length=1000)
    def __str__(self):
        return self.patient
    
class Prescription(models.Model):
    MedicalRecord=models.ForeignKey(MedicalRecord,on_delete=models.CASCADE)
    medication=models.CharField(max_length=1000)
    dosage=models.CharField(max_length=1000)
    instruction=models.CharField(max_length=1000)
    def __str__(self):
        return self.MedicalRecord
    
