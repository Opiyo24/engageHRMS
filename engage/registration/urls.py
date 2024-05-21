from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='registration-index'),
    path('register/', views.register, name='registration-register'),
    path('login/', views.user_login, name='registration-login'),
    path('logout/', views.user_logout, name='registration-logout'),
    path('profile/', views.user_profile, name='registration-profile'),
    path('e-register/', views.employee, name='registration-employee'),
    path('em-profile/', views.employee_profile, name='registration-em-profile'),
    path('c-register/', views.company, name='registration-company'),
    path('c-profile/', views.company_profile, name='registration-c-profile'),
]