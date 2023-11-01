from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_manager.views import profile_form, profile_extra_form, registration_view, login_view, logout_view
from user_manager.viewsets import UserProfileViewSet, UserExtraViewSet, UserProfilePageViewSet

router = DefaultRouter()
router.register('user_profile', UserProfileViewSet, basename="user_profile")
router.register('user_extra', UserExtraViewSet, basename="user_extra")

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<str:username>/', UserProfilePageViewSet.as_view({'get': 'list'}), name='profile'),
    path('', UserProfilePageViewSet.as_view({'get': 'list'}), name='profile'),
]
