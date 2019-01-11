
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse 
from .form import*
from .models import*
# Create your views here.(request):
        
def homepage(request):
        return render(request, 'home.html') 

def gmail(request):
    send_mail(
    'Subject here',
    'Here is the message.',
    'shalinisingh199605@gmail.com',
    ['shalinisingh199605@gmail.com'],
    fail_silently=False,)
    return render(request, 'gmail.html') 

def base(request):
        return render(request, 'base.html')
def login(request):
        return render(request, 'login.html')
def relogin(request):
        return render(request, 'home.html')

#form content

# def form():
#     obj=admin.object.all()
  
def newuser(request):
    formdata = studentform()

    if request.method=='POST':
        formdata=studentform(request.POST)
        if formdata.is_valid():
            formdata.save()
            return HttpResponse("your registration succesfully completed")
            return render(request, 'home.html')
        else:
            print(formdata.errors)

    return render(request, 'new_user.html', {'udata':formdata}) 

# def newuser(request):
#     return render(request, 'new_user.html')