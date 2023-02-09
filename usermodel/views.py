from django.shortcuts import render, redirect
from django.apps import apps
from django.views.generic import TemplateView
# Create your views here.
from .models import User




def getBranchNameList():
    model = apps.get_model('cbrmbllive', 'DimCompany')
    queryset = model.objects.all()
    branchlist = [{'id': x.company_id, 'name': x.company_name} for x in queryset]
    return branchlist


def getDesignations():

    ASSISTANT_OFFICER = 'AO'
    OFFICER = 'OFF'
    EXECUTIVE_OFFICER = 'EO'
    SENIOR_EXECUTIVE_OFFICER = 'SEO'
    PRINCIPAL_OFFICER = 'PO'
    FIRST_ASSISTANT_VICE_PRESIDENT = 'FAVP'
    ASSISTANT_VICE_PRESIDENT = 'AVP'
    FIRST_VICE_PRESIDENT = 'FVP'
    VICE_PRESIDENT = 'VP'
    SENIOR_VICE_PRESIDENT = 'SVP'
    SENIOR_EXECUTIVE_VICE_PRESIDENT = 'SEVP'
    designation_choices = [
        {'id': ASSISTANT_OFFICER, 'desg': 'ASSISTANT OFFICER'},
        {'id':OFFICER, 'desg': 'OFFICER'},
        {'id':EXECUTIVE_OFFICER, 'desg': 'EXECUTIVE OFFICER'},
        {'id':SENIOR_EXECUTIVE_OFFICER, 'desg': 'SENIOR EXECUTIVE OFFICER'},
        {'id':PRINCIPAL_OFFICER, 'desg': 'PRINCIPAL OFFICER'},
        {'id':FIRST_ASSISTANT_VICE_PRESIDENT, 'desg': 'FIRST ASSISTANT VICE PRESIDENT'},
        {'id':ASSISTANT_VICE_PRESIDENT, 'desg': 'ASSISTANT VICE PRESIDENT'},
        {'id':FIRST_VICE_PRESIDENT, 'desg': 'FIRST VICE PRESIDENT'},
        {'id':VICE_PRESIDENT, 'desg': 'VICE PRESIDENT'},
        {'id':SENIOR_VICE_PRESIDENT, 'desg': 'SENIOR VICE PRESIDENT'},
        {'id':SENIOR_EXECUTIVE_VICE_PRESIDENT, 'desg': 'SENIOR EXECUTIVE VICE PRESIDENT'},

    ]

    return designation_choices



class Register(TemplateView):
    template_name = 'registration/register.html'
    model = apps.get_model('cbrmbllive', 'DimCompany')

    def get_context_data(self, **kwargs):
        context = dict()

        context['branchlist'] = getBranchNameList()
        context['designation_choices'] = getDesignations()
        return context

    def post(self,*args, **kwargs):
        email = self.request.POST['email']
        password = self.request.POST['password']
        branch_code = self.request.POST['branchCode']
        branch_object = self.model.objects.get(company_id=branch_code)
        emp_name = self.request.POST['emp_name']
        emp_id = self.request.POST['emp_id']
        designation = self.request.POST['desg']
        mobile_num = self.request.POST['mobile_num']
        User.objects.create_user(email=email,
                                 password=password,
                                 branchCode=branch_code,
                                 branch_name=branch_object.company_name,
                                 emp_name=emp_name,
                                 emp_id=emp_id,
                                 designation=designation,
                                 mobile_num=mobile_num
                                 )
        return redirect('login')


