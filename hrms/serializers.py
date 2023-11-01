from rest_framework import serializers

from hrms.models import Employee, LeaveTracker, Salary, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class LeaveTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveTracker
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'
