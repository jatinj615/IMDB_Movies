from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, UserManager
from rest_framework.test import APIClient, APITestCase


class TestUserViews(APITestCase):


    def setUp(self):
        client = APIClient()
        self.signup_url = reverse('user-signup')
        self.login_url = reverse('user-login')
        self.credentials = {'username': 'trainman', 'password': 'trainman'}
        

    def test_user_signup_POST(self):

        response = self.client.post(self.signup_url, self.credentials)
        self.assertEquals(response.status_code, 201)
    

    def test_user_login_POST(self):

        User.objects.create_user(**self.credentials)
        response = self.client.post(self.login_url, self.credentials)
        self.assertEquals(response.status_code, 200)


