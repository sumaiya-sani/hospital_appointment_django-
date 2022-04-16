from dataclasses import field
from turtle import mode
from rest_framework import serializers
from .models import Doctor




class Doctorserializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields =['id','name','doctor_picture','age','gender','address','specualization','describe']



