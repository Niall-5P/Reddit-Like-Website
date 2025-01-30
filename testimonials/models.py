# testimonials/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator  # Import validators

class Testimonial(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    rating = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),  # Optional: Set minimum rating
            MaxValueValidator(5)   # Set maximum rating to 5
        ]
    )  # Rating is optional but limited to 1-5
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Testimonial by {self.author} on {self.created_on.strftime('%Y-%m-%d')}"
