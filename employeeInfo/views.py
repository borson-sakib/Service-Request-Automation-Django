from django.shortcuts import render
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

# Create your views here.
import requests
import json
import environ

employeeURL= settings.APIURL

FunctionalDesignations = ["HOD","HOB","MOP","DEPUTY HEAD","CREDIT IN-CHARGE","FOREIGN TRADE IN-CHARGE","GB IN-CHARGE","CASH","CASH IN CHARGE"]

def index(request):
    return render(request,'employee_registration.html')

def login(request):
    return render(request,'login.html')


def create_profile(request):
  if request.method == 'POST':
    # Get the uploaded file
    picture = request.FILES['picture']

    # Do something with the file...

    return HttpResponse('Picture uploaded successfully')
  else:
    return render(request,'create_profile.html')

def checkId(request):
    if (request.method == "POST"):
        url = str(employeeURL) + str(request.POST["employeeId"])
        response = requests.post(url)
        response = response.json()
        if response["EmpFunctionalDesignation"] in FunctionalDesignations:
            return HttpResponse(response)
        
        messages.warning(request, 'You are not authorized to Enter')
        return redirect('login')
        # if(request.POST["employeeId"] == "1111"):
        #     return render(request,'employee_registration.html')