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