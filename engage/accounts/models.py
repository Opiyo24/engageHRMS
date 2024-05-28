from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     id = models.AutoField(primary_key=True)

class Company(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    logo = models.ImageField(upload_to='company_logo', default='default.jpg')

    def __str__(self):
        return f"{self.name}"
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
class Title(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
class Contract_type(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.contract_type}"
    
class Position(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


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
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
