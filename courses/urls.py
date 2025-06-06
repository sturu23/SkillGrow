from django.urls import path
from .views import course_list, course_detail

urlpatterns = [
    path('', course_list, name='courses'),
    path('course/<uuid:pk>/', course_detail, name='course_detail'),
]
