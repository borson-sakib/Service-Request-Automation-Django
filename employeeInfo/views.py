from django.shortcuts import render
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *

from .models import *

# Create your views here.
import requests
import json
import environ

# from bs4 import BeautifulSoup



employeeURL= settings.APIURL

FunctionalDesignations = ["HOD","HOB","MOP","DEPUTY HEAD","CREDIT IN-CHARGE","FOREIGN TRADE IN-CHARGE","GB IN-CHARGE","CASH","CASH IN CHARGE"]

@login_required(login_url='/login')
def index(request):

    form = RequestForm()

    return render(request,'test.html',{'form': form})

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
        print(request.POST)
        url = str(employeeURL) + str(request.POST["employeeId"])
        response = requests.post(url)
        response = response.json()

        if response["EmployeeID"] is not None:
            print(request.POST["employeeId"])
            # Get the uploaded file
            
            uploaded_file1 = request.FILES['signature']
            uploaded_file2 = request.FILES['pi']
            # Create a Photo instance using the uploaded file
            # photo = Photo(image=uploaded_file, caption='My photo')
            # photo.save()
            # form = ImageForm(request.POST, request.FILES)
            # if form.is_valid():
            #     form.save()
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
                password=request.POST['password'],
                signature=uploaded_file1,
                pi=uploaded_file2,
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



def service_request(request):
    if(request.method == "POST"):

        print(request.POST)

        Service_request_OBJ = Service_request(
            request_no=request.POST['request_no'],
            date=request.POST['date'],
            employee_name=request.POST['employee_name'],
            branch_code=request.POST['branch_code'],
            department=request.POST['department'],
            mobile_no=request.POST['mobile_no'],
            designation=request.POST['designation'],
            employee_id=request.POST['employee_id'],
            branch_division_name=request.POST['branch_division_name'],
            pa_no=request.POST['pa_no'],
            ip_address=request.POST['ip_address'],
            email=request.POST['email'],
            # from_date = request.POST['from_date'],
            self_type = request.POST['self_type'],
            # to_date = request.POST['to_date'],
            # from_time = request.POST['from_time'],
            # to_time = request.POST['to_time'],
            reason = request.POST['reason'],
            details = request.POST['details'],
            vendor_name = request.POST['vendor_name'],
            name1 = request.POST['name1'],
            contact_number1 = request.POST['contact_number1'],
            name2 = request.POST['name2'],
            contact_number2 = request.POST['contact_number2'],
            # to_date_check = request.POST['to_date_check'],
            # to_time_check = request.POST['to_time_check']
        )

        try:
            Service_request_OBJ.to_date=request.POST['to_date']
        except:
            pass
        
        try:
            Service_request_OBJ.to_date_check=request.POST['to_date_check']
        except:
            pass
    
        try:
            Service_request_OBJ.from_time=request.POST['from_time']
        except:
            pass
    
        try:
            Service_request_OBJ.to_time=request.POST['to_time']
        except:
            pass
      
        try:
            Service_request_OBJ.to_time_check=request.POST['to_time_check']
        except:
            pass
      
        try:
            Service_request_OBJ.from_date=request.POST['from_date']
        except:
            pass

        Service_request_OBJ.save()

        print(request.POST)

        return HttpResponse('Successful')

        # form = RequestForm(request.POST)

        # print(form.data)
        # form.save()

        # if form.is_valid():
        #     print(form.is_valid)
        #     form.save()


    return redirect('index')    



    # request_no;
    # date;
    # employee_name;
    # branch_code;
    # department;
    # mobile_no;
    # designation;
    # employee_id;
    # branch_division_name;
    # pa_no;
    # ip_address;
    # email;
    # self_type;
    # from_date;
    # to_date;
    # from_time;
    # to_time;
    # reason;
    # details;
    # vendor_name;
    # name1;
    # contact_number1;
    # name2;
    # contact_number2;
    # to_date_check;
    # to_time_check