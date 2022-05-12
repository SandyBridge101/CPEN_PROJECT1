from multiprocessing import context
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from . models import logo
#from . forms import loginform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegistrationForm, logoform
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic.edit import CreateView
# Create your views here.

"""
def register(request):
    form=modelform()


    if request.method=='POST':#if there is a request to post
        form=modelform(request.POST)

        if form.is_valid():#if it meets all contraints. mine worked without the brackets
            form.save()

            return redirect('/')
        else:
            form=modelform()



    context={
        'form':form,
    }
    return render(request,'register.html',context)

"""
def register(request):
    pic=logo.objects.all()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
        'pic':pic,
    }
    return render(request, 'register.html', context)



def login(request):
    pic=logo.objects.all()
    if request.method == 'post':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render (request,'login.html', {'error':'You are not logged in!'})
    else:
        #return render(request,'login.html',{})
        return HttpResponse("not Slogged in")


def base(request):
    pic=logo.objects.all()

    context={
        pic:'pic'
    }

    return render(request, 'partials/nav.html', context)

def landing_page(request):
    return render(request,'landingpage.html')