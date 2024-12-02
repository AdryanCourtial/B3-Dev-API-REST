from rest_framework.test import APITestCase
from api.models import Civilites
from django.urls import reverse
from rest_framework import status


class CivilitesTestCase(APITestCase):
    def setUp(self):
        Civilites.objects.create(name="Baptiste")


    def test_languages_post(self):
        """The Civilites Created"""
        url = reverse('get_civilities')  
        response = self.client.post(url, {
            'name' : 'TEST'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        

    def test_languages_get(self):
        """The Civilites Get"""
        url = reverse('get_civilities')  
        response = self.client.get(url)
        langue = Civilites.objects.get(name="Baptiste")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(langue.name, "Baptiste")
