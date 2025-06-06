from django.shortcuts import get_object_or_404, render

from  courses.models import Course

# Create your views here.
def course_list(request):
    from .models import Course
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})