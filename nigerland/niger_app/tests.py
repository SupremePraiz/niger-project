from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

from niger_app import models
from niger_app.api.serializers import SurveyorSerializer, DocumentSerializer

class SurveyorTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username="praiz", password="Password@1234")
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token.access_token))
        
        self.surveyor = models.Surveyor.objects.create(name="praiz",
                                                        email="praiz@gmail.com",
                                                        is_active=True,
                                                        created="2024-07-07T00:43:34.437380Z")
    
    def test_surveyor(self):
        
        data ={
            "name":"praiz",
            "email":"praiz@gmail.com",
            "is_active":"True",
            "created":"2024-07-07T00:43:34.437380Z",
        }
        response = self.client.post(reverse("surveyor"), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_surveyor_list(self):
        response = self.client.get(reverse("surveyor"), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_surveyor_detail(self):
       response = self.client.get(reverse("surveyordetail", args=[self.surveyor.id]), format='json')
       self.assertEqual(response.status_code, status.HTTP_200_OK)
        