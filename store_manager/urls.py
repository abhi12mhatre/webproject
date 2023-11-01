from django.urls import path, include
from rest_framework.routers import DefaultRouter

from store_manager.viewsets import StoreViewSet, ClientViewSet, ProductViewSet, OrderViewSet, StockViewSet, \
    InvoiceViewSet, DashboardViewSet

router = DefaultRouter()
router.register('store', StoreViewSet, basename="store")
router.register('client', ClientViewSet, basename="client")
router.register('invoice', InvoiceViewSet, basename="invoice")
router.register('product', ProductViewSet, basename="product")
router.register('order', OrderViewSet, basename="order")
router.register('stock', StockViewSet, basename="stock")

urlpatterns = [
    path('api/', include(router.urls)),
    path('', DashboardViewSet.as_view({'get': 'list'}), name='store_dashboard'),

]
