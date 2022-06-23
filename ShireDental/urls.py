

from django.urls import URLPattern
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.Home, name="index"),
    path("patient",views.patient, name="patient"),
    path("doctor",views.Doct, name="doctor"),

    path("pricing",views.Pricing, name="pricing"),
    
]