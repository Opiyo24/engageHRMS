from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='registration-index'),
    path('register/', views.register, name='registration-register'),
    path('login/', views.login, name='registration-login'),
]