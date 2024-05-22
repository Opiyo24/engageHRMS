from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='registration-index'),
    # path('register/', views.register, name='registration-register'),
    # path('login/', views.user_login, name='registration-login'),
    # path('logout/', views.user_logout, name='registration-logout'),
] + static(settings.STATIC_URL)