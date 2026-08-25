from django.http import HttpResponse, JsonResponse
from django.conf import settings
from datetime import datetime

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Service_request,User # replace with the name of your model
import logging
logger = logging.getLogger('email_logger')


FunctionalDesignations = ["HOD","HOB","MOP","DEPUTY HEAD","CREDIT IN-CHARGE","FOREIGN TRADE IN-CHARGE","GB IN-CHARGE","CASH","CASH IN CHARGE","IT Management"]

def find_HOX_email(pop):
    try:
        hod_obj = User.objects.filter(Placeofposting=pop,EmpFunctionalDesignation__in=FunctionalDesignations).last()

        return str(hod_obj.username)
    except:
        return None


def send_email(email):
    print(email)
    email = email
    try:
   
        activation_link = 'http://10.99.99.201:8012/ac/login'
        subject = 'New Access/Service Request - Waiting For Approval'
        html_message = render_to_string('verification_email.html', {'activation_link': activation_link})
        plain_message = strip_tags(html_message)
        email_from = settings.EMAIL_HOST_USER
        
        email_message = EmailMessage(subject, html_message, email_from, [email])
        email_message.content_subtype = "html"
        email_message.send()
        
        logger.info(f"{datetime.now()} - Email sent to {email}: {subject}")
        # return JsonResponse({'status': 'success', 'message': f'Email sent to {email}'}, status=200)
    
    except Exception as e:
        print(e)
        logger.error(f"{datetime.now()} - Failed to send email to {email}: {str(e)}")
        # return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        return False