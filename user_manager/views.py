from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UserExtraForm
from .forms import UserProfileForm


@login_required
def profile_form(request):
    userprofile_defaults = {}
    if request.method == 'POST' or request.method == 'PATCH':
        # Handle both POST and PATCH requests
        userprofile_form = UserProfileForm(request.POST if request.method == 'POST' else request.PATCH,
                                           prefix='userprofile')
        if userprofile_form.is_valid():
            userprofile_form.save()
            return render(request, 'templates/user_manager/profile_page.html')
    elif request.GET.get('edit') == 'true':
        # Try to get the user's existing profile if it exists
        try:
            userprofile = request.user.userprofile
            userprofile_defaults = {
                'firstname': userprofile.firstname,
                'middlename': userprofile.middlename,
                'lastname': userprofile.lastname,
                'gender': userprofile.gender,
                'dob': userprofile.dob,
                'email': userprofile.email,
                'address': userprofile.address,
                'phone': userprofile.phone,
                'alternate_phone': userprofile.alternate_phone,
            }
        except:
            pass

    userprofile_form = UserProfileForm(initial=userprofile_defaults, prefix='userprofile')
    return render(request, 'templates/user_manager/profile_form.html',
                  {'userprofile_form': userprofile_form})


@login_required
def profile_extra_form(request):
    if request.method == 'POST':
        userextra_form = UserExtraForm(request.POST, prefix='userextra')
        if userextra_form.is_valid():
            userextra_form.save()
            return render(request, 'templates/user_manager/profile_page.html')
    else:
        userextra_form = UserExtraForm(prefix='userextra')

    return render(request, 'templates/user_manager/profile_extra_form.html',
                  {'userextra_form': userextra_form})


def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        error = validate_registration(username, email, password1, password2)
        if error:
            messages.error(request, error)
        else:
            new_user = User.objects.create_user(username, email, password1)
            new_user.save()
            login(request, new_user)  # Log the user in after registration
            messages.success(request, 'Registration successful.')
            return redirect(request.GET.get('next', 'profile'), username=new_user.username)
    return redirect('profile')


def validate_registration(username, email, password1, password2):
    invalid_usernames = ['admin', 'hrms', 'estate_manager', 'store_manager', 'tour_manager', 'api',
                         'profile_form', 'profile_extra_form', 'register', 'login', 'logout']
    if username in invalid_usernames:
        return 'Username not allowed'
    if password1 != password2:
        return 'Password Mismatch'
    if User.objects.filter(username=username).exists():
        return 'Username already taken'
    return None


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            username = user.username
            goto = request.GET.get('next')
            if not goto or goto == '/':
                goto = 'profile'
            return redirect(goto, username=username)
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return redirect(request.GET.get('next', 'profile'))


def logout_view(request):
    logout(request)
    return redirect(request.GET.get('next', 'profile'))
