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
from django.db.models import Q


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
    user_id = request.user.EmployeeID
    service_requests = Service_request.objects.filter(application_status=300)
    count = service_requests.count()



    queryset = network_analysts_group.objects.filter(network_analyst_employee_id=user_id)
    if queryset.exists():
        analyst_user = True
        # events = Service_request.objects.all()
        events = sorted(Service_request.objects.all(), key=lambda event: event.days_left())

        context = {'events': events}
        # return render(request, 'template.html', {'exists': True})
    else:
        analyst_user = False
        events = Service_request.objects.all()
        context = {'events': events}

        # return render(request, 'template.html', {'exists': False})

    return render(request,'landing.html',{'Username':name,'analyst':analyst_user,'events': events,'count':count})

@login_required(login_url='/login')
def index(request,id):

    if Service_request.objects.filter(Q(employee_id=request.user.EmployeeID) & Q(form_no=id)).exists():

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
        print(id)
        return render(request,'test.html',{'form': form,'user_object':obj,'authorizer':authorizer,'form_no':id})

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

def service_request(request):
    if(request.method == "POST"):


            if Service_request.objects.filter(Q(employee_id=request.user.EmployeeID) & Q(form_no=request.POST['form_no'])).exists():

                messages.success(request, 'Your Form is Already Submitted !')

                return redirect('access_request_user')

            else:
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

                    source_ip = request.POST['source_ip'],
                    destination_ip =request.POST['destination_ip'],
                    destination_port =request.POST['destination_port'],
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
        return render(request,'access_request_user.html',{'access_request':obj})



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
    # Get the entry using the entry_id
    entry = get_object_or_404(Service_request, pk=entry_id)

    # Delete the entry
    entry.delete()

    # Redirect to the page showing the remaining entries
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

            job_id = request.GET.get('id'),
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


def addCategory(request):
    
    if (request.method=="POST"):
        
        print(request.POST)
    
    form = ServiceCategoryForm()
    
    return render(request,'admin/serviceCategory.html',{'form':form})
