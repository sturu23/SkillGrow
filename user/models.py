from django.db import models
from datetime import date
from django.contrib.auth.models import User
import uuid
from .choices import ROLE_CHOICES

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # ✅ UUID as primary key
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=False)
    last_name = models.CharField(max_length=30, blank=True, null=False)
    email = models.EmailField(max_length=254, blank=True, null=False)
    date_of_birth = models.DateField(null=False, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    courses = models.ManyToManyField('courses.Course', blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None
