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
        return f"{self.company_name} Profile."
