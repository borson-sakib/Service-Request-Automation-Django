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
    path('view_only/<str:pid>/', view_only, name="view_only"),
    path('form/<str:id>/', index, name="index"),
    path('form67', form67, name="form67"),
    path('approver_list', approver_list, name="approver_list"),
    path('form_submissions', show_entries, name="form_submissions"),
    path('', landing, name="landing"),
    path('create_profile', create_profile, name="create_profile"),
    path('login', loginView, name="login"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('checkId', checkId, name="checkId"),
    path('service_request', service_request, name="service_request"),
    path('access_request', access_request, name="access_request"),
    path('access_request_user', access_request_user, name="access_request_user"),
    path('task_execute', task_execute, name="task_execute"),
    path('actions/<str:variable_1>/', actions, name="actions"),
    # path('fetch_user/<str:userid>/', fetch_user, name="fetch_user"),
    path('fetch', fetch, name="fetch"),
    path('reg_test', reg_test, name="reg_test"),
    path('user_list', user_list, name="user_list"),
    path('update/<int:user_id>/', user_update, name='user_update'),
    path('delete/<int:user_id>/', user_delete, name='user_delete'),
    path('set_user_another_table/<int:user_id>/', set_user_another_table, name='set_user_another_table'),
    path('delete-entry/<int:entry_id>/', delete_entry, name='delete_entry'),
    path('update-entry/<int:entry_id>/', update_entry, name='update_entry'),
    
    
    
    path('gini', gini, name="gini"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


