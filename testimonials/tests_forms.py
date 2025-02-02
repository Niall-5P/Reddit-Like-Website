from django.test import TestCase
from .forms import TestimonialForm

class TestTestimonialForm(TestCase):
    def test_form_is_valid_with_valid_data(self):
        """
        Verify that the form is valid when content is provided
        and rating is within the allowed range (1 to 5).
        """
        form = TestimonialForm(data={
            'content': 'This website is awesome!',
            'rating': 4
        })
        self.assertTrue(form.is_valid())

    def test_form_is_valid_with_no_rating(self):
        """
        Verify that rating can be left blank, since it's optional.
        """
        form = TestimonialForm(data={
            'content': 'This is a testimonial without rating.'
        })
        self.assertTrue(form.is_valid(), msg="Form should be valid with no rating.")

    def test_form_is_invalid_without_content(self):
        """
        'content' is required. If it's blank, the form should be invalid.
        """
        form = TestimonialForm(data={
            'content': '',
            'rating': 3
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid without content.")

    def test_form_is_invalid_with_rating_below_minimum(self):
        """
        The rating field has a MinValueValidator(1), so rating < 1 should be invalid.
        """
        form = TestimonialForm(data={
            'content': 'Decent website.',
            'rating': 0
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid with rating below 1.")

    def test_form_is_invalid_with_rating_above_maximum(self):
        """
        The rating field has a MaxValueValidator(5), so rating > 5 should be invalid.
        """
        form = TestimonialForm(data={
            'content': 'Great website!',
            'rating': 6
        })
        self.assertFalse(form.is_valid(), msg="Form should be invalid with rating above 5.")
