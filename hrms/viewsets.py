from django.shortcuts import render
from rest_framework import viewsets

from hrms.models import LeaveTracker, Employee, Salary, Company
from hrms.serializers import EmployeeSerializer, SalarySerializer, LeaveTrackerSerializer, CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class LeaveTrackerViewSet(viewsets.ModelViewSet):
    queryset = LeaveTracker.objects.all()
    serializer_class = LeaveTrackerSerializer


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class DashboardViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        print(12)
        context = {'nav_link': 'templates/hrms/nav.html'}
        return render(request, 'templates/hrms/dashboard.html', context=context)
