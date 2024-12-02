from rest_framework.test import APITestCase
from api.models import States
from django.urls import reverse
from rest_framework import status


class StatesTestCase(APITestCase):
    def setUp(self):
        States.objects.create(name="Baptiste")


    def test_languages_post(self):
        """The States Created"""
        url = reverse('get_states')  
        response = self.client.post(url, {
            'name' : 'TEST'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        

    def test_languages_get(self):
        """The States Get"""
        url = reverse('get_languages')  
        response = self.client.get(url)
        langue = States.objects.get(name="Baptiste")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(langue.name, "Baptiste")
