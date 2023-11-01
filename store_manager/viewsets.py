from django.shortcuts import render
from rest_framework import viewsets

from estate_manager.serializers import InvoiceSerializer
from store_manager.models import Store, Client, Product, Order, Stock, Invoice
from store_manager.serializers import StoreSerializer, ProductSerializer, OrderSerializer, StockSerializer, \
    ClientSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class DashboardViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        context = {'nav_link': 'templates/store_manager/nav.html'}
        return render(request, 'templates/store_manager/dashboard.html', context=context)
