from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from .utils import ldapcheck


# Create your models here.

# Not Using BranchList

class UserManager(BaseUserManager):
    def create_user(self, email,
                    password=None,
                    Placeofposting=None,
                    EmployeeName=None,
                    EmployeeID=None,
                    EmployeeDesignation=None,
                    EmpFunctionalDesignation=None,
                    signature=None,
                    pi=None,
                    ):
        """
        Creates and saves a User with the given email and password from mblbd domain .
        """

        # print(email)
        # print(password)
        if not email:
            raise ValueError('Users must have an email address')

        if ldapcheck(email, password):
            '''
            ldap password and email check successfull and user id exists.
            '''

            user = self.model(
                email=self.normalize_email(email),
            )

            user.set_password('')
            if Placeofposting is not None:
                user.EmployeeName = EmployeeName
                user.EmployeeDesignation = EmployeeDesignation
                user.EmpFunctionalDesignation = EmpFunctionalDesignation
                user.Placeofposting = Placeofposting
                user.EmployeeID = EmployeeID
                user.signature = signature
                user.pi = pi
            # else:
            #     raise ValueError("Branch Code is mandatory")
            user.save(using=self._db)
            return user
        else:
            raise ValueError('Username or password Does not Match with specified domain')

    def create_staffuser(self,
                         email,
                         password,
                         emp_name,
                         emp_id,
                         designation,
                         mobile_num,):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            branchCode='BD0010101',
            branch_name='Main Branch',
            emp_name=emp_name,
            emp_id=emp_id,
            designation=designation,
            mobile_num=mobile_num,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,
                         email,
                         password,
                         emp_name,
                         emp_id,
                         designation,
                         mobile_num,
                         ):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            branchCode='BD0010101',
            branch_name='Main Branch',
            emp_name=emp_name,
            emp_id=emp_id,
            designation=designation,
            mobile_num=mobile_num,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):


    # username = models.CharField(unique=True, max_length=100)
    EmployeeName = models.CharField(max_length=200)
    EmployeeDesignation = models.CharField(max_length=200)
    EmpFunctionalDesignation = models.CharField(max_length=200)
    Placeofposting = models.CharField(max_length=200)
    EmployeeID = models.CharField(unique=True,max_length=11,primary_key=True)
    signature = models.ImageField(upload_to='images/signatures',blank=True)
    pi = models.ImageField(upload_to='images/pi',blank=True)


    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # branch_code = models.CharField(max_length=200, null=True)  # branch_code for now
    # branch_name = models.CharField(max_length=200, null=True)  # branch_name for now
    # emp_name = models.CharField(max_length=200, null=True)  # emp_name for now
    # emp_id = models.CharField(max_length=200, null=True)  # emp_id for now
    # mobile_num = models.CharField(max_length=20, null=True)  # emp_id for now
    # designation = models.CharField(max_length=5, choices=designation_choices, default=ASSISTANT_OFFICER, null=True)

    # branch_code = models.ForeignKey('cbrmbllive.DimCompany', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    # notice the absence of a "Password field", that is built in.
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['EmployeeID']  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    def save(self, *args, **kwargs):
        self.signature.name = self.EmployeeID + '_signature.jpg'
        self.pi.name = self.EmployeeID + '_pi.jpg'
        super().save(*args, **kwargs)
  
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
