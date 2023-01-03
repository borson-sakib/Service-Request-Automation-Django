from django.shortcuts import render
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
import requests
import json
import environ

employeeURL= settings.APIURL

FunctionalDesignations = ["HOD","HOB","MOP","DEPUTY HEAD","CREDIT IN-CHARGE","FOREIGN TRADE IN-CHARGE","GB IN-CHARGE","CASH","CASH IN CHARGE"]

@login_required(login_url='/login')
def index(request):
    return render(request,'employee_registration.html')

def loginView(request):
    if (request.method == "POST"):
        username = request.POST['employeeId']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')

        messages.warning(request, 'You are not authorized to Enter')      
        
        return redirect('login')
    else:
        return render(request,'login.html')


def create_profile(request):
    if request.method == 'POST':
        url = str(employeeURL) + str(request.POST["employeeId"])
        response = requests.post(url)
        response = response.json()

        if response["EmployeeID"] is not None:
            print(request.POST["employeeId"])
            # Get the uploaded file
            

            # Do something with the file...
            
            funcDesig="others"
            if response["EmpFunctionalDesignation"] in FunctionalDesignations:
                funcDesig=response["EmpFunctionalDesignation"]

            User.objects.create_user(
                username=request.POST['employeeId'], 
                EmployeeName=response["EmployeeName"],
                EmployeeDesignation=response["EmpDesignation"],
                EmpFunctionalDesignation=funcDesig,
                Placeofposting=response["POP"],
                EmployeeID=response["EmployeeID"],
                password=request.POST['password']
                )
                
            messages.success(request, 'User Creation Successful')
            
            return redirect('login')

        else:
            messages.success(request, 'Unable to find the user ID !')
            return redirect('create_profile')
    else:
        return render(request,'create_profile.html')

def checkId(request):
    if (request.method == "POST"):
        url = str(employeeURL) + str(request.POST["employeeId"])
        response = requests.post(url)
        # response = response.json()
        # if response["EmpFunctionalDesignation"] in FunctionalDesignations:
        return HttpResponse(response.text)
        
        # messages.warning(request, 'You are not authorized to Enter')
        # return redirect('login')
        # if(request.POST["employeeId"] == "1111"):
        #     return render(request,'employee_registration.html')

