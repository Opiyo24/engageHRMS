from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company_account(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100, default='')
    password2 = models.CharField(max_length=100, default='')
    company_address = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    company_phone = models.CharField(max_length=100)
    company_website = models.URLField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logo', default='default.jpg')

    def __str__(self):
        return f"{self.company_name}"
    
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_abbreviation = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.department_name}"
    
class Title(models.Model):
    title_name = models.CharField(max_length=100)
    title_abbreviation = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.title_name}"
    
class Contract_type(models.Model):
    contract_type = models.CharField(max_length=100)
    contract_abbreviation = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.contract_type}"


class Employee(models.Model):
    DEPARTMENTS = [
        ('HR', 'Human Resources'),
        ('FIN', 'Finance'),
        ('IT', 'Information Technology'),
        ('SALES', 'Sales'),
        ('MARK', 'Marketing'),
        ('PROD', 'Production'),
        ('LOG', 'Logistics'),
        ('ADM', 'Administration'),
        ('MNG', 'Management'),
    ]

    CONTRACT_TYPE = [
        ('FULL', 'Full Time'),
        ('PART', 'Part Time'),
        ('ATT', 'Attachment'),
        ('CON', 'Contract'),
        ('INT', 'Internship'),
    ]

    TITLES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof'),
        ('Eng', 'Eng'),
    ]
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, choices=TITLES, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=DEPARTMENTS, null=True)
    contract_type = models.CharField(max_length=100, choices=CONTRACT_TYPE, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to='profile_picture', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
