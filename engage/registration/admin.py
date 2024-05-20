from django.contrib import admin
from .models import User, Company, Employee

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    list_filter = ('created_at', 'updated_at')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyid', 'companyname', 'created_at', 'updated_at')
    search_fields = ('companyname',)
    list_filter = ('created_at', 'updated_at')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'companyname', 'employeeusername', 'created_at', 'updated_at')
    search_fields = ('employeeusername', 'user__username', 'companyname__companyname')
    list_filter = ('created_at', 'updated_at')
