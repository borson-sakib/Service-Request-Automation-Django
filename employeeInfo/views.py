from django.shortcuts import render


def index(request):
    return render(request,'employee_registration.html')