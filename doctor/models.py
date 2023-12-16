from django.db import models

# Create your models here.
class DoctorInfo(models.Model):
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    def __str__(self):
        return self.f_name
    