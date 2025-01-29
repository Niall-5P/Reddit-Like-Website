# testimonials/models.py

from django.db import models
from django.contrib.auth.models import User

class Testimonial(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    rating = models.IntegerField(null=True, blank=True)  # optional
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Testimonial by {self.author} on {self.created_on.strftime('%Y-%m-%d')}"
