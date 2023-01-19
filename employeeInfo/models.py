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
   

