from django.contrib import admin

from estate_manager.models import Invoice, Estate, Tenant


# Register your models here.
class EstateAdmin(admin.ModelAdmin):
    list_display = ['owner'] + [field.name for field in Estate._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['owner']


class TenantAdmin(admin.ModelAdmin):
    list_display = ['estate'] + [field.name for field in Tenant._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['estate']


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['estate', 'tenant'] + [field.name for field in Invoice._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['estate', 'tenant']


admin.site.register(Estate, EstateAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(Invoice, InvoiceAdmin)
