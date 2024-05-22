from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='accounts-signup'),
    path('company/', views.company_creation, name='company-signup'),
    path('logged/', views.logged, name='company-logged'),
]