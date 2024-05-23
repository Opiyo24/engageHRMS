# myapp/admin.py
from django.contrib import admin
from .models import *

class CompanyAccountAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_email', 'company_phone', 'company_website')
    search_fields = ('company_name', 'company_email')
    list_filter = ('company_name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'department', 'title', 'contract_type')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'title', 'contract_type')

admin.site.register(Company_account, CompanyAccountAdmin)
admin.site.register(Department)
admin.site.register(Title)
admin.site.register(Contract_type)
admin.site.register(Employee)
