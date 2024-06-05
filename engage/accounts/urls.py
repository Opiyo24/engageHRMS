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
    path('add_dept/<int:pk>/delete', views.delete_dept, name='delete_dept'),
    path('edit_dept/<int:pk>/', views.DepartmentUpdateView.as_view(), name='edit_dept'),
    path('edit_title/<int:pk>/', views.TitleUpdateView.as_view(), name='edit_title'),
    path('edit_contract_type/<int:pk>/', views.ContractTypeUpdateView.as_view(), name='edit_contract_type'),
    path('edit_position/<int:pk>/', views.PositionUpdateView.as_view(), name='edit_position'),
    path('edit_employee/<int:pk>/', views.EmployeeUpdateView.as_view(), name='edit_employee'),
    path('delete_position/<int:pk>/', views.delete_position, name='delete_position'),
    path('delete_contract_type/<int:pk>/', views.delete_contract_type, name='delete_contract_type'),
    path('delete_title/<int:pk>/', views.delete_title, name='delete_title'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('delete_employee/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('profile/', views.dashboard, name='dashboard'),
    path('calendar/', views.calendar, name='calendar'),
]