import datetime
from multiprocessing import context
from urllib import response
from .models import studentproject
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse,Http404
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required(login_url='/login/')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='/login/')
def file_open(request):
    file=studentproject.objects.all()   #raw('select * from "studentdashboard_studentproject" ')
    context={
        'file':file,
    }
    return render(request,'file.html',context)

def logout_request(request):
    logout(request)
    messages.info(request,"you are logged out")
    return redirect('login/')

def home(request):
    logout(request)
    messages.info(request,"you are logged out")
    return redirect('/')


#{% url 'open-file' project.projectfile %}
