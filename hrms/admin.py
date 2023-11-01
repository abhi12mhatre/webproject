from django.contrib import admin

from hrms.models import Company, LeaveTracker, Employee, Salary


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['manager', 'company'] + [field.name for field in Employee._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['manager', 'company']


class LeaveTrackerAdmin(admin.ModelAdmin):
    list_display = ['employee'] + [field.name for field in LeaveTracker._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['employee']


class SalaryAdmin(admin.ModelAdmin):
    list_display = ['employee'] + [field.name for field in Salary._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['employee']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(LeaveTracker, LeaveTrackerAdmin)
admin.site.register(Salary, SalaryAdmin)
