from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField()
    birth_date = models.DateField()
    rec_created_by = models.DateField(auto_now=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    remarks = models.CharField(max_length=1000, blank=True, null=True)
    designation = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
          return self.firstname