from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class Student1(models.Model):
    fullname = models.CharField( unique=True, max_length=100)
    email = models.EmailField(max_length=100)
# Create your models here.
