
# Create your views here.
from django.shortcuts import render

def landing(request):
    return render(request, 'core/landing.html')

def contact(request):
    return render(request, 'core/contact.html')