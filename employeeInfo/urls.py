from telnetlib import LOGOUT
from django.contrib import admin
from django.urls import path
from .views import *
# from .utils import *
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.middleware import AuthenticationMiddleware

urlpatterns = [

    path('form1', index, name="index"),
    path('', landing, name="landing"),
    path('create_profile', create_profile, name="create_profile"),
    path('login', loginView, name="login"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('checkId', checkId, name="checkId"),
    path('service_request', service_request, name="service_request"),
    path('access_request', access_request, name="access_request"),
    path('access_request_user', access_request_user, name="access_request_user"),
    path('actions/<str:variable_1>/', actions, name="actions"),
    # path('fetch_user/<str:userid>/', fetch_user, name="fetch_user"),
    path('fetch', fetch_user, name="fetch"),
    path('reg_test', reg_test, name="reg_test"),
    
    
    
    path('gini', gini, name="gini"),


]


