from django.shortcuts import render
from rest_framework import viewsets

from tour_manager.models import Tour, Customer, Package, Invoice
from tour_manager.serializers import InvoiceSerializer, PackageSerializer, CustomerSerializer, TourSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class DashboardViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        context = {'nav_link': 'templates/tour_manager/nav.html'}
        return render(request, 'templates/tour_manager/dashboard.html', context=context)
