from email import message
from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse
from .models import Appointment, Doctor, Patient
from .forms import ApointmentForm, DoctorForm, PatientForm

def Home(request):
   
   return render(request,"shiredental/base.html")
    
            
def Doct(request):
   Dform = Doctor.objects.all()
   context = {'Dform':Dform}
   return render(request, 'shiredental/doctor.html', context)



            
            
def patient(request):
   pform = PatientForm
   if request.method == 'POST':
      pform.save
      print(request.POST)
      pform = PatientForm(request.POST)
      if pform.is_valid():
         pform.save(commit=True)
      else:
         print("Error")         
   context = {'pform':pform}
   return render(request, 'shiredental/patient.html',{'pform': pform})
    
   

def Pricing(request):
   return render(request, 'shiredental/pricing.html')




    

