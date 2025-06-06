from django.db import models
import uuid

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='course_photos/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    
    instructor = models.ForeignKey(
        'user.Profile',  # Fixed app label here
        on_delete=models.SET_NULL,
        null=True,
        related_name='instructed_courses'
    )
    
    students = models.ManyToManyField(
        'user.Profile',  # Fixed app label here too
        related_name='enrolled_courses',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('course_detail', kwargs={'pk': self.pk})
