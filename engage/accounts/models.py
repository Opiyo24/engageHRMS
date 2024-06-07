from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     id = models.AutoField(primary_key=True)

class Company(models.Model):
    """
    Model for a company.
    """
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
    """
    Model for a department.
    """
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
class Title(models.Model):
    """
    Model for a title.
    """
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
class Contract_type(models.Model):
    """
    Model for a contract type.
    """
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
class Position(models.Model):
    """
    Model for a position.
    """
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    """
    Model for an employee.
    """
    STATUS = [
        ('Active', 'Active'),
        ('Leave', 'Leave')
    ]
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=100, unique=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    contract_type = models.ForeignKey(Contract_type, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to='profile_picture', default='default.jpg')
    status = models.CharField(max_length=100, choices=STATUS, default='Active')
    shift = models.CharField(max_length=100, default='TBD')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
