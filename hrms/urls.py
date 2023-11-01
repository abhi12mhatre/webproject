from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hrms.viewsets import CompanyViewSet, EmployeeViewSet, SalaryViewSet, LeaveTrackerViewSet, DashboardViewSet

router = DefaultRouter()
router.register('company', CompanyViewSet, basename="company")
router.register('employee', EmployeeViewSet, basename="employee")
router.register('leaves', LeaveTrackerViewSet, basename="leaves")
router.register('salary', SalaryViewSet, basename="salary")

urlpatterns = [
    path('api/', include(router.urls)),
    path('', DashboardViewSet.as_view({'get': 'list'}), name='hrms_dashboard'),

]
