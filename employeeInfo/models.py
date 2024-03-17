from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.


class User(AbstractUser):
    # username = models.EmailField(unique=True, primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    EmployeeName = models.CharField(max_length=200)
    EmployeeDesignation = models.CharField(max_length=200)
    EmpFunctionalDesignation = models.CharField(max_length=200)
    Placeofposting = models.CharField(max_length=200)
    EmployeeID = models.CharField(unique=True,max_length=11,primary_key=True)
    signature = models.ImageField(upload_to='images/signatures',blank=True)
    pi = models.ImageField(upload_to='images/pi',blank=True)

    def save(self, *args, **kwargs):
        self.signature.name = self.EmployeeID + '_signature.jpg'
        self.pi.name = self.EmployeeID + '_pi.jpg'
        super().save(*args, **kwargs)
    # username = None
    # email = None
    first_name = None
    last_name = None

    objects = UserManager()

   

    # USERNAME_FIELD = "mobileNumber"
    REQUIRED_FIELDS = []
    
class ServiceCategory(models.Model):
    service_category = models.CharField(max_length=50)
    category_id = models.CharField(max_length=20)
    
    def __str__(self):
        return self.service_category
    
    def save(self, *args, **kwargs):
        # Check if the instance is being created for the first time
        if not self.pk:
            # Get the latest category_id from the database
            latest_category = ServiceCategory.objects.order_by('-category_id').first()

            if latest_category:
                # Extract the number part of the latest category_id and increment it
                new_category_number = str(int(latest_category.category_id) + 1).zfill(3)
            else:
                # If no categories exist yet, start with '001'
                new_category_number = '001'

            # Assign the new category_id to the instance
            self.category_id = new_category_number

        super().save(*args, **kwargs)

class Service_request(models.Model):
    form_no = models.CharField(max_length=100,blank=True)
    service_request_id= models.CharField(max_length=100,null=True)
    service_title = models.CharField(max_length=200,null=True)
    request_no = models.CharField(max_length=100, primary_key=True)
    date = models.DateField(max_length=100)
    employee_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    branch_division_name = models.CharField(max_length=100)
    pa_no = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    request_for = models.CharField(max_length=100,blank=True,choices=[
        ('access', 'Access'),
        ('service', 'Service'),
        
    ])
    self_type = models.CharField(max_length=100,blank=True,
        
        choices=[
            ('self', 'Self'),
            ('selfwithservice', 'Self with Service'),
            ('serviceprovider', 'Service Provider'),
            ('team', 'Team'),
            ('visitor', 'Visitor')
        ],
    )
    from_date = models.DateField(max_length=100,blank=True)
    to_date = models.DateField(max_length=100,null=True)
    to_date_check = models.BooleanField(max_length=100,default=False)
    from_time = models.TimeField(max_length=100,null=True)
    to_time = models.TimeField(max_length=100,null=True)
    to_time_check = models.BooleanField(max_length=100,default=False)
    reason = models.CharField(max_length=500,blank=True)
    details = models.CharField(max_length=500,blank=True)
    tools_device_required =  models.CharField(max_length=200,blank=True)


    source_ip =models.CharField(max_length=100,blank=True) 
    destination_ip =models.CharField(max_length=100,blank=True) 
    destination_port =models.CharField(max_length=100,blank=True) 
    physical_activity_area =models.CharField(max_length=300,blank=True) 
    chng_exec_req_id =models.CharField(max_length=100,blank=True) 

    vendor_name = models.CharField(max_length=100,blank=True)
    name1 = models.CharField(max_length=100,blank=True)
    contact_number1 = models.CharField(max_length=100,blank=True)
    name2 = models.CharField(max_length=100,blank=True)
    contact_number2 = models.CharField(max_length=100,blank=True)

    team_name1 = models.CharField(max_length=100,blank=True)
    team_emp_id1 = models.CharField(max_length=100,blank=True)
    team_name2 = models.CharField(max_length=100,blank=True)
    team_emp_id2 = models.CharField(max_length=100,blank=True)
    team_name3 = models.CharField(max_length=100,blank=True)
    team_emp_id3 = models.CharField(max_length=100,blank=True)
    team_name4 = models.CharField(max_length=100,blank=True)
    team_emp_id4 = models.CharField(max_length=100,blank=True)
    team_lead = models.CharField(max_length=100,blank=True)
    team_lead_epmloyee_id = models.CharField(max_length=100,blank=True)

    approved_by_HOB = models.CharField(max_length=100,null=True,default="No")
    approved_by_CISO = models.CharField(max_length=100,null=True,default="No")
    approved_by_CTO = models.CharField(max_length=100,null=True,default="No")
    application_status = models.IntegerField(max_length=100,null=True,default="0")
    
    
    category = models.CharField(max_length=50,null=True)

   
   
    
    def days_left(self):
        from datetime import date
        today = date.today()
        if self.to_date:
            delta = self.to_date - today
            return delta.days
        return 0  # or any other default value if date is not set
   
class Service_request_form_67(models.Model):
    pass
    # form_no = models.CharField(max_length=100,blank=True)

    # service_request_id= models.CharField(max_length=100,null=True)
    # service_title = models.CharField(max_length=200,null=True)
    # request_no = models.CharField(max_length=100)
    # date = models.DateField(max_length=100)
    # employee_name = models.CharField(max_length=100)
    # branch_code = models.CharField(max_length=100)
    # department = models.CharField(max_length=100)
    # mobile_no = models.CharField(max_length=100)
    # designation = models.CharField(max_length=100)
    # employee_id = models.CharField(max_length=100)
    # branch_division_name = models.CharField(max_length=100)
    # pa_no = models.CharField(max_length=100)
    # ip_address = models.CharField(max_length=100)
    # email = models.EmailField(max_length=100)
    # self_type = models.CharField(max_length=100,blank=True,
        
    #     choices=[
    #         ('self', 'Self'),
    #         ('selfwithservice', 'Self with Service'),
    #         ('serviceprovider', 'Service Provider'),
    #         ('team', 'Team'),
    #         ('visitor', 'Visitor')
    #     ],
    # )
    # from_date = models.DateField(max_length=100,blank=True)
    # to_date = models.DateField(max_length=100,null=True)
    # to_date_check = models.BooleanField(max_length=100,default=False)
    # from_time = models.TimeField(max_length=100,null=True)
    # to_time = models.TimeField(max_length=100,null=True)
    # to_time_check = models.BooleanField(max_length=100,default=False)
    # reason = models.CharField(max_length=500,blank=True)
    # details = models.CharField(max_length=100,blank=True)

    # tools_device_required =  models.CharField(max_length=200,blank=True)

    # source_ip =models.CharField(max_length=100,blank=True) 
    # destination_ip =models.CharField(max_length=100,blank=True) 
    # destination_port =models.CharField(max_length=100,blank=True) 
    # physical_activity_area =models.CharField(max_length=300,blank=True) 
    # chng_exec_req_id =models.CharField(max_length=100,blank=True) 

    # vendor_name = models.CharField(max_length=100,blank=True)
    # name1 = models.CharField(max_length=100,blank=True)
    # contact_number1 = models.CharField(max_length=100,blank=True)
    # name2 = models.CharField(max_length=100,blank=True)
    # contact_number2 = models.CharField(max_length=100,blank=True)

    # team_name1 = models.CharField(max_length=100,blank=True)
    # team_emp_id1 = models.CharField(max_length=100,blank=True)
    # team_name2 = models.CharField(max_length=100,blank=True)
    # team_emp_id2 = models.CharField(max_length=100,blank=True)
    # team_name3 = models.CharField(max_length=100,blank=True)
    # team_emp_id3 = models.CharField(max_length=100,blank=True)
    # team_name4 = models.CharField(max_length=100,blank=True)
    # team_emp_id4 = models.CharField(max_length=100,blank=True)
    # team_lead = models.CharField(max_length=100,blank=True)
    # team_lead_epmloyee_id = models.CharField(max_length=100,blank=True)

    # approved_by_HOB = models.CharField(max_length=100,null=True,default="No")
    # approved_by_CISO = models.CharField(max_length=100,null=True,default="No")
    # approved_by_CTO = models.CharField(max_length=100,null=True,default="No")
    # application_status = models.IntegerField(max_length=100,null=True,default="0")

    

class status_code(models.Model):
    status_code = models.CharField(max_length=10)
    status_meaning = models.CharField(max_length=100)
    forwarded_to = models.CharField(max_length=100,null=True)

class operations_log(models.Model):
    service_request_employee_id= models.CharField(max_length=100)
    service_request_id= models.CharField(max_length=100)
    service_request_time= models.DateTimeField(max_length=100)
    approved_hod= models.CharField(max_length=100,default='0')
    approved_hod_at= models.DateTimeField(max_length=100,null=True)
    approved_ciso= models.CharField(max_length=100,default='0')
    approved_ciso_at= models.DateTimeField(max_length=100,null=True)
    approved_cto= models.CharField(max_length=100,default='0')
    approved_cto_at= models.DateTimeField(max_length=100,null=True)
    executed= models.CharField(max_length=100,default='0')
    executed_at= models.DateTimeField(max_length=100,null=True)
    current_status=models.CharField(max_length=100,default='0')

class network_analysts_group(models.Model):

    network_analyst_employee_id= models.CharField(max_length=100,null=True)
    network_analyst_name= models.CharField(max_length=100,null=True)
    network_analyst_email= models.CharField(max_length=100,null=True)

class execution_log(models.Model):
    job_id= models.CharField(max_length=100,null=True)
    job_ref = models.ForeignKey(Service_request, on_delete=models.CASCADE, related_name='execution_logs', null=True)
    executed_by= models.CharField(max_length=100,null=True)
    approved_by= models.CharField(max_length=100,null=True)
    job_description= models.CharField(max_length=100,null=True)
    execution_status= models.CharField(max_length=100,null=True)
    execution_remarks= models.CharField(max_length=100,null=True)
    revoke_date_time= models.CharField(max_length=100,null=True)
    revoked_by= models.CharField(max_length=100,null=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.executed_by:
            self.executed_by_name = User.objects.get(EmployeeID=self.executed_by).EmployeeName
        else:
            self.executed_by_name = None
            
    def save(self, *args, **kwargs):
        if not self.job_id:
            # Get the maximum job_id value from existing objects
            max_job_id = execution_log.objects.all().aggregate(models.Max('job_id'))['job_id__max']

            # Set the new job_id
            if max_job_id:
                new_job_id = str(int(max_job_id) + 1).zfill(6)
            else:
                new_job_id = '100001'
                
            self.job_id = new_job_id
            
            
        super().save(*args, **kwargs)

class ApproverList(models.Model):
    employee_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    approver_level = models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.employee_id  # or any other field you want to display

# class service_status(models.Model):



