import json

from django.shortcuts import render
from rest_framework import viewsets

from .models import UserProfile, UserExtra, Experience
from .serializers import UserProfileSerializer, UserExtraSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def list(self, request, *args, **kwargs):
        return super(UserProfileViewSet, self).list(request, *args, **kwargs)


class UserExtraViewSet(viewsets.ModelViewSet):
    queryset = UserExtra.objects.all()
    serializer_class = UserExtraSerializer


class UserProfilePageViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request, username='abhi12mhatre'):
        if request.user.is_authenticated:
            username = request.user.username
        try:
            user_profile_obj = UserProfile.objects.get(user__username=username)
            user_extra_queryset = UserExtra.objects.filter(userprofile=user_profile_obj, status=0).values('key',
                                                                                                          'value')
            experience = list(Experience.objects.filter(userprofile=user_profile_obj).only(
                'from_date', 'to_date', 'company_name', 'position', 'description'
            ).order_by("-from_date"))
        except UserProfile.DoesNotExist:
            user_profile_obj = None
            user_extra_queryset = {}
            experience = None
        user_extra = {}
        for extra in user_extra_queryset:
            user_extra[extra['key']] = json.loads(extra['value'])

        context = {'request': request,
                   'user_profile': user_profile_obj,
                   'user_extra': user_extra,
                   'experience': experience,
                   'nav_link': 'templates/user_manager/nav.html'}
        return render(request, 'templates/user_manager/profile_page.html', context=context)
