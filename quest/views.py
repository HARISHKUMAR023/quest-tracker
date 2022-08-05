import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
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
        return render(request,"dashboard/main.html",messages.success(request,'COMPANY CEO'))
       except  ceo.DoesNotExist as e:
         messages.success(request,'username / password invaid..!')  
  return render(request,'index.html') 
def man(request):
  if request.method == 'POST':
       try:
        userdel =  manager.objects.get(email=request.POST['email'],password=request.POST['password'])
        print("username=",userdel)
        request.session['email']=userdel.email
        
        return render(request,"dashboard/main.html",messages.success(request, 'Manager'))
       except  manager.DoesNotExist as e:
         messages.success(request,'username / password invaid..!')  
  return render(request,'manager.html') 
def logout(request):
  
  return redirect(request,'logout.html')  


  
  

  

def main(request):
  return render(request,'index.html')   
def dash(request):
  return render(request , 'dashboard/main.html')  
