# testimonials/forms.py

from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['content', 'rating']
        # You can include 'approved' if you want users to set it, 
        # or keep it hidden if only admins can approve
