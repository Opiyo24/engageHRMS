from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='accounts-home'),
    # path('signup/', views.signup, name='accounts-signup'),
    path('company/', views.company_creation, name='company-signup'),
    path('company_login/', views.login_view, name='company-login'),
    path('logout/', views.logout_view, name='logout'),
    path('logged/', views.logged, name='company-logged'),
    path('company_set_up_intro/', views.company_set_up_intro, name='company_set_up_intro'),
    path('company_set_up/', views.company_set_up, name='company_set_up'),
    path('add_dept/', views.add_dept, name='add_dept'),
    path('add_title/', views.add_title, name='add_title'),
    path('add_position/', views.add_position, name='add_position'),
    path('add_contract_type/', views.add_contract_type, name='add_contract_type'),
    path('remove_dept/', views.remove_dept, name='remove_dept'),
    path('remove_position/', views.remove_position, name='remove_position'),
    path('remove_contract_type/', views.remove_contract_type, name='remove_contract_type'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('remove_employee/', views.remove_employee, name='remove-employee'),
    path('employees/', views.employees, name='employees'),
    path('profile/', views.dashboard, name='company-profile'),
    path('calendar/', views.calendar, name='calendar'),
    path('add_activity/', views.add_activity, name='add-activity'),
    path('remove_activity/', views.remove_activity, name='remove-activity'),
    path('activities/', views.activities, name='activities'),
]