# user/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.email = user.email  # sync email
            profile.save()
            profile_form.save_m2m()  # for ManyToMany field courses
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # change to your login url name
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, 'user/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('landing')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
    else:
        return render(request, 'user/login.html')
    

def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'user/profile.html', {
        'profile_form': profile_form,
    })

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('landing')  # change to your landing page url name


def user_courses(request):
    # Placeholder for user courses view
    # You can implement logic to fetch and display user's courses here
    return render(request, 'user/user_courses.html')



def user_settings(request):
    user = request.user
    profile = user.profile  # assuming you have a OneToOneField Profile model related to User

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        profile_pic = request.FILES.get('profile_pic')

        # Basic validation (you can expand this)
        if not username or not email:
            messages.error(request, "Username and email cannot be empty.")
            return render(request, 'user_settings.html', {'user': user})

        # Update user fields
        user.username = username
        user.email = email
        user.save()

        # Handle profile picture upload
        if profile_pic:
            # Optional: delete old pic if exists
            if profile.profile_pic:
                profile.profile_pic.delete(save=False)

            profile.profile_pic = profile_pic
            profile.save()

        messages.success(request, "Your settings have been updated.")
        return redirect('user_settings')

    # GET request: render form with current user info
    return render(request, 'user/user_settings.html', {'user': user})