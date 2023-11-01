from django.contrib import admin

from store_manager.models import Store, Client, Stock, Invoice, Order, Product


# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Store._meta.get_fields() if not field.is_relation]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['store'] + [field.name for field in Client._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['store']


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields() if not field.is_relation]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'store'] + [field.name for field in Order._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['product', 'store']


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['order'] + [field.name for field in Invoice._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['order']


class StockAdmin(admin.ModelAdmin):
    list_display = ['product', 'store'] + [field.name for field in Stock._meta.get_fields() if not field.is_relation]
    raw_id_fields = ['product', 'store']


admin.site.register(Store, StoreAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Stock, StockAdmin)
