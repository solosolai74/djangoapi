from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User, Group  # user

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__' 
