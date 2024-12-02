from rest_framework.test import APITestCase
from api.models import Categories
from django.urls import reverse
from rest_framework import status


class CategoriesTestCase(APITestCase):
    def setUp(self):
        Categories.objects.create(name="Baptiste")


    def test_categories_post(self):
        """The Categories Created"""
        url = reverse('get_categories')  
        response = self.client.post(url, {
            'name' : 'TEST'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        

    def test_categories_get(self):
        """The Categories Get"""
        url = reverse('get_categories')  
        response = self.client.get(url)
        langue = Categories.objects.get(name="Baptiste")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(langue.name, "Baptiste")
