from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("patientInfo",patientInfoView)
router.register("medicalRecords",medicalrecordView)
router.register("prescriptions",prescriptionview)

urlpatterns = [
    path("patients/",include(router.urls))
]
