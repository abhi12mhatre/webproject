from django.contrib import admin

from tour_manager.models import Package, Customer, Tour, Invoice


# Register your models here.

class PackageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Package._meta.get_fields() if not field.is_relation]


class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.get_fields() if not field.is_relation]


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['tour'] + [field.name for field in Invoice._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['tour']


class TourAdmin(admin.ModelAdmin):
    list_display = ['package', 'customer'] + [field.name for field in Tour._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['package', 'customer']


admin.site.register(Package, PackageAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Tour, TourAdmin)
