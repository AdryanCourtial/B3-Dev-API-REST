from rest_framework.test import APITestCase
from api.models import Languages
from django.urls import reverse
from rest_framework import status


class LanguagesTestCase(APITestCase):
    def setUp(self):
        Languages.objects.create(name="Baptiste")


    def test_languages_post(self):
        """The Languages Created"""
        url = reverse('get_languages')  
        response = self.client.post(url, {
            'name' : 'TEST'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        

    def test_languages_get(self):
        """The Languages Get"""
        url = reverse('get_languages')  
        response = self.client.get(url)
        langue = Languages.objects.get(name="Baptiste")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(langue.name, "Baptiste")
