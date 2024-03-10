from django import forms
from .models import User,Service_request

from django import forms
from django.forms import ModelForm
from .models import ApproverList
from .models import ServiceCategory



class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = '__all__'


class RequestForm(forms.ModelForm):
    request_no = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control form-control-sm', 'placeholder': 'Please enter request no.', 'aria-label': 'LabelRequestNo', 'aria-describedby': 'addon-wrapping'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class': 'form-control', 'placeholder': 'Please enter date', 'aria-label': 'LabelDate', 'aria-describedby': 'addon-wrapping'}))
    employee_name = forms.CharField(initial='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter employee name', 'aria-label': 'LabelEmployeeName', 'aria-describedby': 'addon-wrapping'}))
    branch_code = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Please enter branch code', 'aria-label': 'LabelBranchCode', 'aria-describedby': 'addon-wrapping'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Please enter department', 'aria-label': 'LabelDepartment', 'aria-describedby': 'addon-wrapping'}))
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Please enter mobile no.', 'aria-label': 'LabelMobileNo', 'aria-describedby': 'addon-wrapping'}))
    designation = forms.CharField(initial='',widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Please enter designation', 'aria-label': 'LabelDesignation', 'aria-describedby': 'addon-wrapping'}))
    employee_id = forms.CharField(initial='',widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Please enter employee id', 'aria-label': 'LabelEmployeeID', 'aria-describedby': 'addon-wrapping'}))
    branch_division_name = forms.CharField(initial='',widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Please enter branch/ division name', 'aria-label': 'LabelBranchDivisionName', 'aria-describedby': 'addon-wrapping'}))
    pa_no = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Please enter PA No.', 'aria-label': 'LabelPANo', 'aria-describedby': 'addon-wrapping'}))
    ip_address = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Please enter IP Address', 'aria-label': 'LabelEmail', 'aria-describedby': 'addon-wrapping'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Please enter Email', 'aria-label': 'LabelPANo', 'aria-describedby': 'addon-wrapping'}))
    request_for = forms.ChoiceField(widget=forms.Select({'class':'form-control'}),
        choices=[
        ('access', 'Access'),
        ('service', 'Service'),
        
    ])
    choices_category = [(category.category_id, category.service_category) for category in ServiceCategory.objects.all()]
    
    category = forms.ChoiceField(widget=forms.Select({'class':'form-control'}),choices=choices_category)
    
    self_type = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'form-check-input','placeholder':'Requested for'}),
        choices=[
            ('self', 'Self'),
            ('selfwithservice', 'Self with Service'),
            ('serviceprovider', 'Service Provider'),
            ('team', 'Team'),
            ('visitor', 'Visitor')
        ],
        required=True,
    )
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'name': 'from-date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'name': 'to-date', 'id': 'to-date'}))
    to_date_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'name': 'to-date-check', 'id': 'to-date-check'}), required=False,initial=False)
    from_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'name': 'from-time', 'id': 'from-time'}))
    to_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'name': 'to-time', 'id': 'to-time'}))
    # to_time_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'name': 'to-time-check', 'id': 'to-time-check','value':'True'}),required=False,initial=False)
    reason = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'reason of request'}))
    details = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Details of Access/Service'}))
    tools_device_required = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Details of Access/Service'}))
    
    source_ip = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Source IP'}))
    destination_ip = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Destination IP'}))
    destination_port = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Destination Port'}))
    physical_activity_area = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Physical Activity Area'}))
    chng_exec_req_id = forms.CharField(widget=forms.TextInput(attrs={'value':'xyz','class': 'form-control', 'placeholder': 'Change/Execution Request ID'}))
    
    
    vendor_name = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Please enter Vendor Name', 'aria-label': 'LabelRequestNo', 'aria-describedby': 'addon-wrapping'}))
    name1 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Name'}))
    contact_number1 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Contact Number'}))
    name2 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Name'}))
    contact_number2 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Contact Number'}))
    
    team_name1 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Team Member Name'}))
    team_emp_id1 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Employee ID'}))
    
    team_name2 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Team Member Name'}))
    team_emp_id2 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Employee ID'}))
    
    team_name3 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Team Member Name'}))
    team_emp_id3 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Employee ID'}))
    
    team_name4 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Team Member Name'}))
    team_emp_id4 = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Employee ID'}))
    
    team_lead = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Name', 'aria-label': 'LabelRequestNo', 'aria-describedby': 'addon-wrapping'}))
    team_lead_epmloyee_id = forms.CharField(widget=forms.TextInput(attrs={'value':'','class': 'form-control form-control-sm', 'placeholder': 'Employee ID'}))

    
    # to_date_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'name': 'to-date-check', 'id': 'to-date-check'}), required=False)
    # to_time_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'name': 'to-time-check', 'id': 'to-time-check'}), required=False)

    # def is_valid(self) -> bool:
    #     self.to_date_check='1' 
    #     self.to_time_check='1' 
    #     return super().is_valid()
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)

        # Set the 'required' attribute for the 'email' field to False
        self.fields['vendor_name'].required = False
        self.fields['name1'].required = False
        self.fields['contact_number1'].required = False
        self.fields['name2'].required = False
        self.fields['contact_number2'].required = False
        self.fields['team_name1'].required = False
        self.fields['team_emp_id1'].required = False
        self.fields['team_name2'].required = False
        self.fields['team_emp_id2'].required = False
        self.fields['team_name3'].required = False
        self.fields['team_emp_id3'].required = False
        self.fields['team_name4'].required = False
        self.fields['team_emp_id4'].required = False
        self.fields['team_lead'].required = False
        self.fields['team_lead_epmloyee_id'].required = False
        # self.fields['category'].queryset = ServiceCategory.objects.all()

    class Meta:
        model = Service_request

        fields = '__all__'




class ApproverListForm(forms.ModelForm):
    APPROVER_LEVEL_CHOICES = [
        ('primary', 'Primary Approver'),
        ('secondary', 'Secondary Approver'),
        ('final', 'Final Approver'),
    ]

    employee_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    approver_level = forms.ChoiceField(choices=APPROVER_LEVEL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
   
    class Meta:
        model = ApproverList
        fields = ['employee_id', 'designation', 'role', 'approver_level']
        
        
        
class ServiceCategoryForm(forms.ModelForm):
    service_category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Category Name','id':'category'}))
    class Meta:
        model = ServiceCategory
        fields = ['service_category']