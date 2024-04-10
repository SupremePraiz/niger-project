from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegistrationTests(APITestCase):
    def test_register(self):
        data = {
            "username":"testcase",
            "email":"testcaseexample@example.com", 
            "password":"NewPassword@123",
            "password2":"NewPassword@123",
        }
        response = self.client.post(reverse("register"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class LoginTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='example', password="NewPassword@123")
        self.user.save()
        
    def test_login(self):
        data={
            "username": "example",
            "password": "NewPassword@123"
        }
        
        response = self.client.post(reverse('token_obtain_pair'), data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        