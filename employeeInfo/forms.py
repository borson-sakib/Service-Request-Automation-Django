from django import forms
from .models import User,Service_request

from django import forms
from django.forms import ModelForm


class RequestForm(forms.ModelForm):
    request_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter request no.', 'aria-label': 'LabelRequestNo', 'aria-describedby': 'addon-wrapping'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class': 'form-control', 'placeholder': 'Please enter date', 'aria-label': 'LabelDate', 'aria-describedby': 'addon-wrapping'}))
    employee_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter employee name', 'aria-label': 'LabelEmployeeName', 'aria-describedby': 'addon-wrapping'}))
    branch_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter branch code', 'aria-label': 'LabelBranchCode', 'aria-describedby': 'addon-wrapping'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter department', 'aria-label': 'LabelDepartment', 'aria-describedby': 'addon-wrapping'}))
    mobile_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter mobile no.', 'aria-label': 'LabelMobileNo', 'aria-describedby': 'addon-wrapping'}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter designation', 'aria-label': 'LabelDesignation', 'aria-describedby': 'addon-wrapping'}))
    employee_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter employee id', 'aria-label': 'LabelEmployeeID', 'aria-describedby': 'addon-wrapping'}))
    branch_division_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter branch/ division name', 'aria-label': 'LabelBranchDivisionName', 'aria-describedby': 'addon-wrapping'}))
    pa_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter PA No.', 'aria-label': 'LabelPANo', 'aria-describedby': 'addon-wrapping'}))
    ip_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter IP Address', 'aria-label': 'LabelEmail', 'aria-describedby': 'addon-wrapping'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter Email', 'aria-label': 'LabelPANo', 'aria-describedby': 'addon-wrapping'}))
    
    self_type = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
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
    to_date_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'name': 'to-date-check', 'id': 'to-date-check'}), required=False)
    from_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'name': 'from-time', 'id': 'from-time'}))
    to_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'name': 'to-time', 'id': 'to-time'}))
    to_time_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'name': 'to-time-check', 'id': 'to-time-check'}), required=False)
    reason = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'reason of request'}))
    details = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Details of Access/Service'}))
    vendor_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter Vendor Name', 'aria-label': 'LabelRequestNo', 'aria-describedby': 'addon-wrapping'}))
    name1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Name'}))
    contact_number1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Contact Number'}))
    name2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Name'}))
    contact_number2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Contact Number'}))
    # to_date_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'name': 'to-date-check', 'id': 'to-date-check'}), required=False)
    # to_time_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'name': 'to-time-check', 'id': 'to-time-check'}), required=False)

    # def is_valid(self) -> bool:
    #     self.to_date_check='1' 
    #     self.to_time_check='1' 
    #     return super().is_valid()

    class Meta:
        model = Service_request

        fields = '__all__'