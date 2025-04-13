from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestimonialViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.create_url = reverse("testimonial_create")
        self.list_url = reverse("testimonial_list")
    
    def test_anonymous_user_cannot_create_testimonial(self):
        """
        Anonymous (not logged in) users should be redirected or forbidden from creating a testimonial.
        """
        response = self.client.get(self.create_url)
        self.assertIn(response.status_code, [302, 403])

    def test_logged_in_user_can_create_testimonial(self):
        """
        Logged-in users should be able to successfully create a testimonial.
        """
        self.client.login(username="testuser", password="testpass")
        post_data = {"content": "A great experience!", "rating": 5}
        response = self.client.post(self.create_url, post_data)
        self.assertEqual(response.status_code, 302)  # typically a redirect after success
        self.assertRedirects(response, self.list_url)
