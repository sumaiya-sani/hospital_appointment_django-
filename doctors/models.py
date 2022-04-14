from audioop import maxpp
from hashlib import blake2b
from pydoc import describe
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save







class Doctor(models.Model):
    CENDER=(
        ('Male','Male'),
        ('Female','Female'),
    )

    specualization=(
        ('Dermatologist','Dermatologist'),
        ('dentist','dentist'),
    )

    name=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    doctor_picture=models.ImageField(null=True,blank=True,upload_to="images/Doctor")
    age=models.CharField(max_length=200,blank=True,null=True)
    gender=models.CharField(max_length=50,choices=CENDER,default='Male')
    address=models.CharField(max_length=500, blank=True,null=True)
    specualization=models.CharField(max_length=500 ,blank=True,null=True,choices= specualization,default='Dermatologist')
    describe=models.TextField()
    activate=models.BooleanField(default=False)
    



    def create_profile(sender,**kwargs):
     if kwargs['created']:
        Doctor.objects.create(name=kwargs['instance'])
    post_save.connect(create_profile,sender=User)  


    def save_profile(sender, instance, **kwargs):
     instance.Doctor.save()

     


    
    def __str__(self):
        return str(self.name)


