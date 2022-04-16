from django import views
from django.urls import path
from django.contrib import admin
from doctors import views

app_name="doctors"

urlpatterns = [
    path('doctors_list/',views.doctor_list,name="doctors_list"),
    path('appontment/<int:pk>/',views.appointment,name="appointment"),
    path('home/',views.home,name="home"),
    path('sucess/<int:pk>/',views.appointment,name="appointment"),
    path('doctors_api/',views.doctors_api),
    path('doctor/<int:id>/',views.doctor),

    
    ]