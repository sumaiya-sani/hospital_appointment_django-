import email
from email import message
from msilib.schema import ListView
from pyexpat import model
from tempfile import template
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from doctors.models import Doctor





def doctor_list(request):
   
   doctors=Doctor.objects.filter(activate=True)
   
   
   if request.method=="POST":
       massage_name=request.POST['massage-name']
       message_email=request.POST['email-name']
       massage=request.POST['massage'] 
       send_mail( 
        massage_name,#subjaect
        message_email,#massage
        massage,#from email
        ['sumaiyathani@gmail.com'],#to email
        
         )
  

    

       return render(request,"Doctors_list.html",{'doctors':doctors,'massage_name': massage_name })
   else:
        return render(request,"Doctors_list.html",{'doctors':doctors })







def home(request):
    
    return render(request,'home.html')    

def appointment(request, pk):

    doctors=Doctor.objects.get(id=pk)
    
   
   
    if request.method=="POST":
       first_name=request.POST['first-name']
       last_name=request.POST['last-name']
       phone_namber=request.POST['phone-number']
       email= request.POST['email']
       date=request.POST['date'] 
       time=request.POST['time'] 
       massage=request.POST['massage'] 
       appointment='Name:'+first_name+'Last_name:'+last_name +'Phone:'+phone_namber+'Email:' +email+'Date:'+date+ 'Time:'+time+'Massage:'+massage 
       send_mail( 
        first_name,#subjaect
        appointment, #massage
        email,#from email
        ['sumaiyathani@gmail.com'],#to email
        
         )
  

    
       return render(request,'appointment.html', {'doctors':doctors , 
        'first_name':first_name ,
        'last_name': last_name ,
        'phone_namber':phone_namber,
        'email': email,
        'date':date,
        'massage':massage,
        }) 
    else:
          return render(request,"appointment.html",{'doctors':doctors })






   


  

    

  
   