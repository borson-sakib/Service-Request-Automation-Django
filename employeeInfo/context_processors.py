

from .models import *

def analyst_user(request):
    
    analyst_user = False
    try:
        queryset = network_analysts_group.objects.filter(network_analyst_employee_id=request.user.EmployeeID)
        if queryset.exists():
            analyst_user = True
                        
    except:
        analyst_user = False
    
    
    return {'analyst': analyst_user}