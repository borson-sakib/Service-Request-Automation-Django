from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, BranchList

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('emp_name','emp_id','designation','mobile_num', 'email','branch_code',  'staff', 'admin')


# @admin.register(BranchList)
# class BranchListAdmin(admin.ModelAdmin):
#     list_display = ('branchCode', 'branchIpAddress', 'branchName', 'branchMnemonic')
