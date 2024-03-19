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
from  .functions import *
from  .oracle_db import *
from  .backends import *
from django.db.models import Q
import cx_Oracle


from .models import *

# Create your views here.
import requests
import json
import environ

# from bs4 import BeautifulSoup



employeeURL= settings.APIURL

FunctionalDesignations = ["HOD","HOB","MOP","DEPUTY HEAD","CREDIT IN-CHARGE","FOREIGN TRADE IN-CHARGE","GB IN-CHARGE","CASH","CASH IN CHARGE","IT Management","CISO"]

@login_required(login_url='/login')
def landing(request):
    name = request.user.EmployeeName
    service_requests = Service_request.objects.filter(application_status=300)
    count = service_requests.count()



    return render(request,'landing.html',{'Username':name,'count':count})

@login_required(login_url='/login')
def index(request,id=None):
    
    if id is not None:
        context= form_navigator(request.user.EmployeeID,id)
        return render(request,'test.html',context)
        
    if request.GET.get('empid'):
        print(request.GET.get('empid'))
        print(request.GET.get('form_no'))
        context= form_navigator(request.GET.get('empid'),request.GET.get('form_no'))
        return render(request,'test.html',context)
    
        
    
    # if Service_request.objects.filter(Q(employee_id=request.user.EmployeeID) & Q(form_no=id)).exists():

    #     messages.success(request, 'Your Form is Already Submitted !')
    #     return redirect('access_request_user')
    # else:
    #     obj = User.objects.get(EmployeeID=request.user.EmployeeID)
    #     authorizer = False
    #     if obj.EmpFunctionalDesignation in FunctionalDesignations:
    #         authorizer = True

    #     form = RequestForm(initial={'employee_name': obj.EmployeeName,'designation':obj.EmployeeDesignation,'employee_id':obj.EmployeeID,'branch_division_name':obj.Placeofposting})
        
        

@login_required(login_url='/login')
def form67(request):

    if(Service_request_form_67.objects.filter(employee_id=request.user.EmployeeID).exists()):
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
        return render(request,'form67.html',{'form': form,'user_object':obj,'authorizer':authorizer})

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
        # print(request.POST)
        url = str(employeeURL) + str(request.POST["employeeId"])
        response = requests.post(url)
        # print("-------------------------------------")
        # print(response)
        response = response.json()

        if response["EmployeeID"] is not None:
            # print(request.POST["employeeId"])
            # print(request.POST["EmpFunctionalDesignation"])
            # Get the uploaded file
            
            uploaded_file1 = request.FILES['signature']
            uploaded_file2 = request.FILES['pi']

            print(uploaded_file1)
            print(uploaded_file2)
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
                # User.objects.create_user(
                #     username=request.POST['email'], 
                #     EmployeeName=response["EmployeeName"],
                #     EmployeeDesignation=response["EmpDesignation"],
                #     EmpFunctionalDesignation=funcDesig,
                #     Placeofposting=response["POP"],
                #     EmployeeID=response["EmployeeID"],
                #     password=request.POST['password'],
                #     signature=uploaded_file1,
                #     pi=uploaded_file2,
                #     )
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

from django.utils.crypto import get_random_string
from datetime import datetime



def service_request(request):
    if(request.method == "POST"):
        
        store_request(request)

        return redirect('access_request_user')
        
        
        # obj = Service_request.objects.filter(employee_id=request.user.EmployeeID).all()

        # return render(request,'access_request_user.html',{'access_request':obj})

    return redirect('index')    



def access_request(request):
    
    #IF user is Authorizer
    if(request.user.EmpFunctionalDesignation in FunctionalDesignations):
        
        if(request.user.EmployeeID=='20091007002'):
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
        obj_others = Service_request.objects.filter(submitted_by=request.user.EmployeeID).exclude(employee_id=request.user.EmployeeID).all()
        return render(request,'access_request_user.html',{'access_request':obj,'access_request_others':obj_others})



def access_request_user(request):

    obj = Service_request.objects.filter(employee_id=request.user.EmployeeID).all()

    return render(request,'access_request_user.html',{'access_request':obj})


def actions(request,variable_1):

    if(request.user.EmployeeID=='20091007002'):
        request_no = variable_1
        obj = get_object_or_404(Service_request, request_no=request_no)
        obj.approved_by_CISO = 'Yes'
        obj.application_status = '200'
        obj.save()
        return redirect('access_request')
    elif(request.user.EmployeeID=='20210701001'):
        request_no = variable_1
        obj = get_object_or_404(Service_request, request_no=request_no)
        obj.approved_by_CTO = 'Yes'
        obj.application_status='300'
        obj.save()
        return redirect('access_request')
    else:
        request_no = variable_1
        obj = get_object_or_404(Service_request, request_no=request_no)
        obj.approved_by_HOB = 'Yes'
        obj.application_status = '100'
        obj.save()
        return redirect('access_request')


def gini(request):

    return render(request,'service_tabs.html')


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def fetch(request):

    if request.method == 'POST':

        if User.objects.filter(EmployeeID=str(request.POST.get("employeeId"))).exists():
            # messages.success(request, 'User is already registered !')
            # return redirect('create_profile')
            response_data = {'result':'userexists'}
            response_data['data'] = 'none' 
            return JsonResponse(response_data)
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
        print('1' + users)
    else:
        users = User.objects.all()
        for user in users:
        # Check if the user's employeeID exists in AnotherTable
            if network_analysts_group.objects.filter(network_analyst_employee_id=user.EmployeeID).exists():
                # If exists, add a field 'analyst' with value True to the user object
                user.analyst = True
            else:
                # If not exists, add a field 'analyst' with value False to the user object
                user.analyst = False
        print(users)
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


   
    print(user.EmployeeID)
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

   
###----------------------------------------------------------###
def show_entries(request):
    # Fetch data from the models
    service_requests = Service_request.objects.filter(application_status=300)
    all_submission = Service_request.objects.all()
    form_67_entries = Service_request_form_67.objects.all()
    exec_log = execution_log.objects.values_list('job_id', flat=True)
    executed_submission = Service_request.objects.filter(request_no__in=exec_log)

    print(exec_log)
    # Render the HTML page with the data
    return render(request, 'form_submissions.html', {
        'service_requests': service_requests,
        'form_67_entries': form_67_entries,
        'exec_log': exec_log,
        'all_submission': all_submission,
        'executed_submission': executed_submission,
    })

def delete_entry(request, entry_id):
    
    delete_any('Service_request',entry_id)

    return redirect('form_submissions')

def update_entry(request, entry_id):
    pass
    # # Get the entry using the entry_id
    # entry = get_object_or_404(Service_request, pk=entry_id)

    # if request.method == 'POST':
    #     # Create an instance of your update form with the submitted data
    #     form = YourUpdateForm(request.POST, instance=entry)
    #     if form.is_valid():
    #         # Save the updated data
    #         form.save()
    #         # Redirect to the page showing the updated entries
    #         return redirect('show_entries')
    # else:
    #     # Populate the form with the existing data of the entry
    #     form = YourUpdateForm(instance=entry)

    # # Render the HTML page with the form for updating the entry
    # return render(request, 'update_entry.html', {'form': form, 'entry': entry})


@login_required(login_url='/login')
def view_only(request,pid):
    Check = False
    obj = User.objects.get(EmployeeID=request.user.EmployeeID)
    applicant_instance = get_object_or_404(Service_request, request_no=pid)
    form = RequestForm(instance=applicant_instance)
    # hod_signature = find_HOX(obj.Placeofposting,pid)
    if(obj.EmpFunctionalDesignation in FunctionalDesignations):
        Check = True
    context = {'hod':find_HOX(applicant_instance.branch_division_name,pid),
                  'cto':find_CTO_status(pid),
                  'ciso':find_CISO_status(pid),
                  'form': form,
                  'user_object':obj,
                  'check':Check}
    # print(hod_signature)
    

    return render(request,'view_only.html',context)




def approver_list(request):
    if request.method == 'POST':
        form = ApproverListForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
    else:
        form = ApproverListForm()

    return render(request, 'approver_list.html', {'form': form})

def task_execute(request):
    
    if execution_log.objects.filter(Q(job_id=request.GET.get('id'))).exists():

        messages.success(request, 'Task Already Executed !')
        return redirect('form_submissions')
    else :
        execution_log_obj = execution_log(

            # job_ref = request.GET.get('id'),
            job_ref = Service_request.objects.get(request_no=request.GET.get('id')),
            executed_by = request.user.EmployeeID,
            job_description = request.GET.get('details'),
            execution_status = request.GET.get('status'),
            execution_remarks = "None"
                            )
        execution_log_obj.save()
        messages.success(request, 'Successfully Executed the task')

        return redirect('form_submissions')
   

def requestaslist(request):
    
    events = sorted(Service_request.objects.all(), key=lambda event: event.days_left())

    context = {'events': events}
    
    return render(request,'admin/listOfRequests.html',context)

from urllib.parse import urlparse, parse_qs

def addCategory(request):
    
    if (request.method=="POST"):
        
        print(request.POST)
        category_already_in_list=[]
        for category in request.POST.getlist('service_category'):

            if not ServiceCategory.objects.filter(service_category=category).exists():
                ServiceCategory.objects.create(service_category=category)
                messages.success(request, 'Category Added to the list !')
            
            messages.success(request, 'Category Alreay in the list !')
        return redirect('addCategory')

    CategoryList=ServiceCategory.objects.all() 
    
    form = ServiceCategoryForm()
    context = {'form':form,'CatList':CategoryList}
    
    return render(request,'admin/serviceCategory.html',context)

def delete_category(request, entry_id):
    # Get the entry using the entry_id
    entry = get_object_or_404(ServiceCategory, category_id=entry_id)

    # Delete the entry
    entry.delete()

    # Redirect to the page showing the remaining entries
    return redirect('addCategory')



def oracle_db_test(request):
    
    data = check_oracle_connection(20210714001)

    return HttpResponse(data)
    
def user_profile(request):
    applicant_instance = get_object_or_404(User, EmployeeID=request.user.EmployeeID)
    form = UserForm(instance=applicant_instance)
    return render(request,'user/user_profile.html',{'form':form})

def execution_logs(request):
    
    data = execution_log.objects.all()
    
    return render(request,'admin/executions.html',{'data':data})

from .fakeuser import *

def fake_user(request):
    
    generate_fake_users(5)
    
    return HttpResponse('Done')

def advanceSearch(request,category=None):
    
    obj= ServiceCategory.objects.all()
    
    if category is not None:
        
        service_request = Service_request.objects.filter(category=category)
        
        return render(request,'admin/advanceSearch.html',{'service_request':service_request,'obj':obj})    
    
    else:
        
        return render(request,'admin/advanceSearch.html',{'obj':obj})
    

def other_user(request,form_no):
    if request.method == 'POST':
        
        other_user=User.objects.filter(EmployeeID=request.POST['employeeid']).first()
        
        # print(other_user.EmployeeName)
        
        return render(request,'user/other_user.html',{'other_user':other_user,'form_no':form_no})
        
    
    return render(request,'user/other_user.html')
    