from enum import unique
from django.db import models
from django.db.models import Deferrable, UniqueConstraint

#Database model


# kani wa database ki dhakhtarka.
class Doctor(models.Model):
    SEX =(
        ('M','Male'),
        ('F','Female'),
    
    )
    FirstName = models.CharField('first name', max_length=120)
    MiddleName = models.CharField('middle name', max_length=120)
    Lastname = models.CharField('last name', max_length=120)
    Telephone = models.IntegerField(unique=True)
    Address = models.CharField(max_length=30)
    Email = models.CharField(max_length=20,unique=True)
    Gender = models.CharField(max_length=1, choices=SEX)
    Speciality = models.CharField(max_length=120)
    
    
    
    def __str__ (self): 
        return self.FirstName
    

class Appointment(models.Model):
    Appo_Number = models.IntegerField()                               #nambarka appointments ka
    Appo_Type = models.CharField(max_length=30) #nooca ballanta
    Appo_Description = models.CharField(max_length=120) #
    Appo_Date = models.DateTimeField()  
    doc_id = models.ForeignKey(Doctor,blank=True,null=True, on_delete=models.CASCADE) # foreignkey
    
    
    def __str__(self):
        return self.Appo_Type  
    
    
    
class Patient(models.Model):
    SEX =(
        ('M','Male'),
        ('F','Female'),
    
    )
    FirstName = models.CharField('first name', max_length=120)
    MiddleName = models.CharField('middle name', max_length=120)
    Lastname = models.CharField('last name', max_length=120)
    Telephone = models.IntegerField(unique=True)
    Address = models.CharField(max_length=30)
    Email = models.CharField(max_length=20,unique=True)
    Gender = models.CharField(max_length=1,choices=SEX)
    doctor = models.ForeignKey(Doctor,blank=False, null=False, on_delete=models.CASCADE)
    Appointments_Available = models.ForeignKey(Appointment,blank=True, null=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.FirstName 
    
   
    
    
       