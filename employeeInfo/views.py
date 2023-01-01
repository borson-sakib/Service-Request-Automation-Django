from django.shortcuts import render
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
import requests
import json


employeeURL= "http://cantexpose/HRM_API/HRM/GetEmpInfo/"
FunctionalDesignations = ["HOD","HOB","MOP","DEPUTY HEAD","CREDIT IN-CHARGE","FOREIGN TRADE IN-CHARGE","GB IN-CHARGE","CASH","CASH IN CHARGE"]

def index(request):
    return render(request,'employee_registration.html')

def login(request):
    return render(request,'login.html')

def checkId(request):
    if (request.method == "POST"):
        url = employeeURL + str(request.POST["employeeId"])
        response = requests.post(url)
        response = response.json()
        if response["EmpFunctionalDesignation"] in FunctionalDesignations:

            print(response["EmpFunctionalDesignation"])
            return HttpResponse(response)
        return HttpResponse("Not Found")
        # if(request.POST["employeeId"] == "1111"):
        #     return render(request,'employee_registration.html')