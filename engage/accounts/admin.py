# myapp/admin.py
from django.contrib import admin
from .models import Company_account

class CompanyAccountAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_email', 'company_phone', 'company_website')
    search_fields = ('company_name', 'company_email')
    list_filter = ('company_name',)

admin.site.register(Company_account, CompanyAccountAdmin)
