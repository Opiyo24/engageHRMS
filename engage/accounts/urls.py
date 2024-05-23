from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accounts-home'),
    path('signup/', views.signup, name='accounts-signup'),
    path('company/', views.company_creation, name='company-signup'),
    path('logged/', views.logged, name='company-logged'),
    path('company_set_up/', views.company_set_up, name='company_set_up'),
    path('profile/', views.profile, name='employee-profile'),
]