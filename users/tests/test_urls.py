from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from users.views import LoginView, CreateUserView


class TestUrls(SimpleTestCase):


    def test_signup_url(self):
        url = reverse('user-signup')
        self.assertEqual(resolve(url).func.view_class, CreateUserView)

    def test_login_url(self):
        url = reverse('user-login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

