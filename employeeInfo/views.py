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
from  .backends import *


from .models import *

# Create your views here.
import requests
import json
import environ

# from bs4 import BeautifulSoup



employeeURL= settings.APIURL

FunctionalDesignations = ["HOD","HOB","MOP","DEPUTY HEAD","CREDIT IN-CHARGE","FOREIGN TRADE IN-CHARGE","GB IN-CHARGE","CASH","CASH IN CHARGE","IT Management"]

@login_required(login_url='/login')
def landing(request):
    name = request.user.EmployeeName

    return render(request,'landing.html',{'Username':name})

@login_required(login_url='/login')
def index(request):

    if(Service_request.objects.filter(employee_id=request.user.EmployeeID).exists()):
        messages.success(request, 'Your Form is Already Submitted !')
        return redirect('access_request_user')
    else:
        obj = User.objects.get(EmployeeID=request.user.EmployeeID)
        authorizer = False
        if obj.EmpFunctionalDesignation in FunctionalDesignations:
            authorizer = True

        print(obj.EmployeeName)
        form = RequestForm(initial={'employee_name': obj.EmployeeName,'designation':obj.EmployeeDesignation,'employee_id':obj.EmployeeID,'branch_division_name':obj.Placeofposting})

        print(obj.EmpFunctionalDesignation)
        return render(request,'test.html',{'form': form,'user_object':obj,'authorizer':authorizer})



def loginView(request):
    if (request.method == "POST"):
        username = request.POST['employeeId']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('landing')

        messages.warning(request, 'You are not authorized to Enter')      
        
        return redirect('login')
    else:
        user=User.objects.filter(is_staff=0).all()
        return render(request,'login.html',{'test':user})


def create_profile(request):
    if request.method == 'POST':
        print(request.POST)
        url = str(employeeURL) + str(request.POST["employeeId"])
        response = requests.post(url)
        response = response.json()

        if response["EmployeeID"] is not None:
            print(request.POST["employeeId"])
            # print(request.POST["EmpFunctionalDesignation"])
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
            email = domainMailCheck(request.POST['email'])

            if ldapcheck(email,request.POST['password']):
                
                User.objects.create_user(
                    username=request.POST['email'], 
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
                
            else:
                messages.success(request, 'Domain Does not match')
                return redirect('create_profile')
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

        if(Service_request.objects.filter(employee_id=request.user.EmployeeID).exists()):

            messages.success(request, 'Your Form is Already Submitted !')

            return redirect('access_request_user')

        else:
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

            

            try:
                Service_request_OBJ.save()
                messages.success(request, 'Form Successfully Submitted and Waiting For Approval')
                
            except:
                messages.success(request, 'Something went wrong. Try again with correct information')

            return redirect('access_request_user')
        

        # obj = Service_request.objects.filter(employee_id=request.user.EmployeeID).all()

        # return render(request,'access_request_user.html',{'access_request':obj})

    return redirect('index')    



def access_request(request):

    #IF user is Authorizer
    if(request.user.EmpFunctionalDesignation in FunctionalDesignations):
        
        if(request.user.EmployeeID=='20190724001'):
            #CISO
            user_requests = Service_request.objects.filter(application_status__gte=100).all()
            return render(request,'access_request_ciso.html',{'user_requests': user_requests})

        elif(request.user.EmployeeID=='20210701001'):
            #CTO
            user_requests = Service_request.objects.filter(application_status__gte=200).all()
            return render(request,'access_request_cto.html',{'user_requests': user_requests})
        else:
            #HOB
            user_requests = Service_request.objects.filter(branch_division_name=request.user.Placeofposting).all()
            return render(request,'access_request_hob.html',{'user_requests': user_requests})
    #IF user is Maker
    else:
        obj = Service_request.objects.filter(employee_id=request.user.EmployeeID).all()
        return render(request,'access_request_user.html',{'access_request':obj})



def access_request_user(request):

    obj = Service_request.objects.filter(employee_id=request.user.EmployeeID).all()

    return render(request,'access_request_user.html',{'access_request':obj})


def actions(request,variable_1):

    if(request.user.EmployeeID=='20190724001'):
        emp_id = variable_1
        obj = get_object_or_404(Service_request, employee_id=emp_id)
        obj.approved_by_CISO = 'Yes'
        obj.application_status = '200'
        obj.save()
        return redirect('access_request')
    elif(request.user.EmployeeID=='20210701001'):
        emp_id = variable_1
        obj = get_object_or_404(Service_request, employee_id=emp_id)
        obj.approved_by_CTO = 'Yes'
        obj.application_status='300'
        obj.save()
        return redirect('access_request')
    else:
        emp_id = variable_1
        obj = get_object_or_404(Service_request, employee_id=emp_id)
        obj.approved_by_HOB = 'Yes'
        obj.application_status = '100'
        obj.save()
        return redirect('access_request')


def gini(request):

    return render(request,'gini.html')


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def fetch(request):
    # print('###########################################################################')
    # # print(request.body)
    # print(request.POST.get('employeeId'))

    # print('###########################################################################')
    # url = str(employeeURL) + str(request.GET["empid"])
    # response = requests.post(url)
    # response = response.json()
    
    
    if request.method == 'POST':
        url = str(employeeURL) + str(request.POST.get("employeeId"))
        response = requests.post(url)
        response_data = {'result': 'success'}
        response_data['data'] = response.json()
        return JsonResponse(response_data)

from .utils import preview_pdf

def fetch_user(request):

    pdf_preview = preview_pdf(request,'20211228046')

    return pdf_preview

def user_list(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.all()
    context = {'users': users, 'query': query}
    return render(request, 'user_list.html', context)

def user_update(request, user_id):
    user = get_object_or_404(User, EmployeeID=user_id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, user_id):
    user = get_object_or_404(User, EmployeeID=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})

def set_user_another_table(request, user_id):
    # get the user object
    user = get_object_or_404(User, EmployeeID=user_id)


   
    print()
    # set the user to another table
    if network_analysts_group.objects.filter(network_analyst_employee_id=user_id).exists():
        analyst_or_none=get_object_or_404(network_analysts_group, network_analyst_employee_id=user_id)
        analyst_or_none.delete()
        messages.success(request, 'Analyst Revoked')
    else:
        try:
            analyst_obj = network_analysts_group(
                        network_analyst_employee_id=user.EmployeeID,
                        network_analyst_name=user.EmployeeName,
                        network_analyst_email=user.username,
                        )
            analyst_obj.save()
            messages.success(request, 'Successfully added user to analyst group')

        except:
            messages.success(request, 'Something went wrong !')

    # redirect to the user list page
    return redirect('user_list')

def reg_test(request):

    return render(request,'reg_test.html')

   

