from django.contrib import admin

from .models import Doctor
from .models import Patient
from .models import Appointment


#from django.utils.html import format_html


admin.site.site_header = "Shire Dental Clinic"

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'doctor', 'Appointments_Available')
 
 
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('FirstName','MiddleName','Speciality','Gender')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('Appo_Number','Appo_Type','Appo_Date','doc_id')         