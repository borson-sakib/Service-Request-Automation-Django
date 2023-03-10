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

class Service_request(models.Model):
    service_request_id= models.CharField(max_length=100,null=True)
    service_title = models.CharField(max_length=200,null=True)
    request_no = models.CharField(max_length=100)
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
    reason = models.CharField(max_length=100,blank=True)
    details = models.CharField(max_length=100,blank=True)
    vendor_name = models.CharField(max_length=100,blank=True)
    name1 = models.CharField(max_length=100,blank=True)
    contact_number1 = models.CharField(max_length=100,blank=True)
    name2 = models.CharField(max_length=100,blank=True)
    contact_number2 = models.CharField(max_length=100,blank=True)
    approved_by_HOB = models.CharField(max_length=100,null=True,default="No")
    approved_by_CISO = models.CharField(max_length=100,null=True,default="No")
    approved_by_CTO = models.CharField(max_length=100,null=True,default="No")
    application_status = models.IntegerField(max_length=100,null=True,default="0")
   

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
    



# class service_status(models.Model):

    
