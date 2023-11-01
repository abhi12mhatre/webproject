from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tour_manager.viewsets import TourViewSet, CustomerViewSet, PackageViewSet, InvoiceViewSet, DashboardViewSet

router = DefaultRouter()
router.register('tour', TourViewSet, basename="tour")
router.register('customer', CustomerViewSet, basename="customer")
router.register('package', PackageViewSet, basename="package")
router.register('invoice', InvoiceViewSet, basename="invoice")

urlpatterns = [
    path('api/', include(router.urls)),
    path('', DashboardViewSet.as_view({'get': 'list'}), name='tour_dashboard'),

]
