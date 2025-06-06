from django.urls import path
from core.views import landing,contact

urlpatterns = [
    path('', landing, name='landing'),
    path('contact/', contact, name='contact'),  # Example for a contact page
    # other paths ...
]
