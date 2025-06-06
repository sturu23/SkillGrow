# user/urls.py

from django.urls import path
from .views import register,login,profile,logout,user_courses, user_settings

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),  # Placeholder for login view
    path('profile/', profile, name='profile'),  # Placeholder for profile view
    path('logout/', logout, name='logout'),  # Placeholder for logout view
    path('user_courses/', user_courses, name='user_courses'),  # Placeholder for user courses view
    path('user_settings/', user_settings, name='user_settings'),  # Placeholder for user settings view
]
