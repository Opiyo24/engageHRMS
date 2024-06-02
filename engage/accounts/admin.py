# myapp/admin.py
from django.contrib import admin
from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'website')
    search_fields = ('name', 'email')
    list_filter = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'department', 'title', 'contract_type')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'title', 'contract_type')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Department)
admin.site.register(Title)
admin.site.register(Contract_type)
admin.site.register(Position)
admin.site.register(Employee, EmployeeAdmin)

