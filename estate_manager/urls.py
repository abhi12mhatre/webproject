from django.urls import path, include
from rest_framework.routers import DefaultRouter

from estate_manager.viewsets import EstateViewSet, TenantViewSet, InvoiceViewSet, DashboardViewSet

router = DefaultRouter()
router.register('estate', EstateViewSet, basename="estate")
router.register('tenant', TenantViewSet, basename="tenant")
router.register('invoice', InvoiceViewSet, basename="invoice")

urlpatterns = [
    path('api/', include(router.urls)),
    path('', DashboardViewSet.as_view({'get': 'list'}), name='estate_dashboard'),



]
