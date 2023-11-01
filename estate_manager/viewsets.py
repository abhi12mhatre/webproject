from django.shortcuts import render
from rest_framework import viewsets

from estate_manager.models import Estate, Tenant, Invoice
from estate_manager.serializers import EstateSerializer, TenantSerializer, InvoiceSerializer


class EstateViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

    
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class DashboardViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        context = {'nav_link': 'templates/estate_manager/nav.html'}
        return render(request, 'templates/estate_manager/dashboard.html', context=context)
