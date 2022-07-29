import django
from django.shortcuts import render
from quest.models import ceo
from quest.models import manager
from django.contrib import messages

# Create your views here.

 
def home(request):  
  if request.method == 'POST':
       try:
        userdel =  ceo.objects.get(email=request.POST['email'],password=request.POST['password'])
        print("username=",userdel)
        request.session['email']=userdel.email
        return render(request,"ceo.html",messages.success(request,'welcome '+ request.POST['email']))
       except  ceo.DoesNotExist as e:
         messages.success(request,'username / password invaid..!')  
  return render(request,'index.html') 
 
 
  

def main(request):
  return render(request,'index.html')   
