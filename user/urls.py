from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('groups',groupView)
router.register('alluser',AlluserView)

urlpatterns = [
    path('login/',login),
    path('register/',register),
    path('user/',include(router.urls))
]
