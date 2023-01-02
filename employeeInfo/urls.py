from telnetlib import LOGOUT
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.middleware import AuthenticationMiddleware

urlpatterns = [

    path('', index, name="index"),
    path('create_profile', create_profile, name="create_profile"),
    path('login', login, name="login"),
    path('checkId', checkId, name="checkId"),
    


]


