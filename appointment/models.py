from django.db import models
from doctor.models import DoctorInfo
from patient.models import PatientInfo

# Create your models here.
class apointment(models.Model):
    patient_name=models.ForeignKey(PatientInfo,on_delete=models.CASCADE)
    doctor=models.ForeignKey(DoctorInfo,on_delete=models.CASCADE)
    appointment_date=models.DateField(auto_now_add=True)
    reason=models.CharField(max_length=300)
    status_choice=[('scheduled','scheduled'),('canceled','canceled'),('completed','completed')]
    status=models.CharField(max_length=9,choices=status_choice,default='scheduled')