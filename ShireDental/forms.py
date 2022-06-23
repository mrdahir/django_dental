from tkinter import Widget
from attr import attrs, field
from django import forms
from django.forms import ModelForm
from .models import *
from django import forms

class ApointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('Appo_Number','Appo_Type','Appo_Description','Appo_Date','doc_id')
   
    Widgets = {
        'Appo_Number':forms.TextInput(attrs={'class':'form-control'}),
        'Appo_Type':forms.TextInput(attrs={'class':'form-control'}), 
        'Appo_Description':forms.TextInput(attrs={'class':'form-control'}),
        'Appo_Date':forms.Select(attrs={'class':'form-control'}),
        'doc_id':forms.Select(attrs={'class':'form-control'}),
        
    }

        
class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('FirstName','MiddleName','Lastname','Telephone','Address','Email','Gender','Speciality')        
        
        widgets ={
            'FirstName':forms.TextInput(attrs={'class':'form-control'}),
            'MiddleName':forms.TextInput(attrs={'class':'form-control'}),
            'Lastname':forms.TextInput(attrs={'class':'form-control'}),
            'Telephone':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Gender':forms.Select(attrs={'class':'form-control'}),
            'Speciality':forms.TextInput(attrs={'class':'form-control'}),
            
        }         
        
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('FirstName','MiddleName','Lastname','Telephone','Address','Email','Gender','doctor','Appointments_Available')        
        
        widgets ={
            'FirstName':forms.TextInput(attrs={'class':'form-control'}),
            'MiddleName':forms.TextInput(attrs={'class':'form-control'}),
            'Lastname':forms.TextInput(attrs={'class':'form-control'}),
            'Telephone':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Gender':forms.Select(attrs={'class':'form-control'}),
            'doctor':forms.Select(attrs={'class':'form-control'}),
            'Appointments_Available':forms.Select(attrs={'class':'form-control'}),
        } 
        
    def clean( self ):
        self.validate_unique()
        cleaned_data = super(PatientForm, self).clean()
        return cleaned_data    