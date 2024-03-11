from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *
from  .utils import *
from  .views import *
from  .oracle_db import *
from  .backends import *
from django.db.models import Q

from django.utils.crypto import get_random_string
from datetime import datetime
from .models import *


def form_navigator(uid,form_no):
    
    obj = User.objects.get(EmployeeID=uid)
    authorizer = False
    if obj.EmpFunctionalDesignation in FunctionalDesignations:
        authorizer = True

    form = RequestForm(initial={'employee_name': obj.EmployeeName,'designation':obj.EmployeeDesignation,'employee_id':obj.EmployeeID,'branch_division_name':obj.Placeofposting})
        
    return {'form': form,'user_object':obj,'authorizer':authorizer,'form_no':form_no}

def generate_unique_id(employee_id, form_number):
    # Get current date and time
    now = datetime.now()
    
    # Format date as YYYYMMDD
    date_str = now.strftime("%Y%m%d")
    
    # Extract the form number part
    form_number_trimmed = form_number.split('-')[-2:]
    form_number_trimmed = '-'.join(form_number_trimmed)
    
    # Generate a random string of length 6
    random_str = get_random_string(length=6)
    
    # Concatenate employee_id, form_no, date, and random string
    unique_id = f"{employee_id}-{form_number_trimmed}-{date_str}-{random_str}"
    
    return unique_id

def store_request(request):
    
    Service_request_OBJ = Service_request(
                    form_no = request.POST['form_no'],
                    request_no=generate_unique_id(request.POST['employee_id'],request.POST['form_no']),
                    # request_no=request.POST['request_no'],
                    date=request.POST['date'],
                    employee_name=request.POST['employee_name'],
                    branch_code=request.POST['branch_code'],
                    department=request.POST['department'],
                    mobile_no=request.POST['mobile_no'],
                    designation=request.POST['designation'],
                    employee_id=request.POST['employee_id'],
                    branch_division_name=request.POST['branch_division_name'],
                    request_for=request.POST['request_for'],
                    ip_address=request.POST['ip_address'],
                    email=request.POST['email'],
                    # from_date = request.POST['from_date'],
                    self_type = request.POST['self_type'],
                    # to_date = request.POST['to_date'],
                    # from_time = request.POST['from_time'],
                    # to_time = request.POST['to_time'],
                    reason = request.POST['reason'],
                    details = request.POST['details'],
                    
                    # source_ip = request.POST['source_ip'],
                    # destination_ip =request.POST['destination_ip'],
                    # destination_port =request.POST['destination_port'],
                    category =request.POST['category'],
                    # tools_device_required =request.POST['tools_device_required'],
                    physical_activity_area =request.POST['physical_activity_area'],
                    chng_exec_req_id =request.POST['chng_exec_req_id'],

                    vendor_name = request.POST['vendor_name'],
                    name1 = request.POST['name1'],
                    contact_number1 = request.POST['contact_number1'],
                    name2 = request.POST['name2'],
                    contact_number2 = request.POST['contact_number2'],

                    team_name1 = request.POST['team_name1'],
                    team_emp_id1 = request.POST['team_emp_id1'],
                    team_name2 = request.POST['team_name2'],
                    team_emp_id2 = request.POST['team_emp_id2'],
                    team_name3 = request.POST['team_name3'],
                    team_emp_id3 = request.POST['team_emp_id3'],
                    team_name4 = request.POST['team_name4'],
                    team_emp_id4 = request.POST['team_emp_id4'],
                    team_lead = request.POST['team_lead'],
                    team_lead_epmloyee_id = request.POST['team_lead_epmloyee_id']
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
    
    try:
        Service_request_OBJ.tools_device_required =request.POST['tools_device_required']

    except:
        pass
    
    try:
        Service_request_OBJ.source_ip = request.POST['source_ip']
        Service_request_OBJ.destination_ip =request.POST['destination_ip']
        Service_request_OBJ.destination_port =request.POST['destination_port']
    except:
        pass

    

    try:
        Service_request_OBJ.save()
        messages.success(request, 'Form Successfully Submitted and Waiting For Approval')
        
    except:
        messages.success(request, 'Something went wrong. Try again with correct information')

    