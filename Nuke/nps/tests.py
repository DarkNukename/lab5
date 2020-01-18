from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, force_authenticate, APITestCase
from .models import NukeList
import json

# Create your tests here.
class Nukes_Tests(APITestCase):

    url = '/api/nukes/'

    def test_Post(self):

        nuke_T = {
            'nps_name': 'Новик',
            'country': 'Россия',
            'factor': 0
            }

        response = self.client.post(self.url, nuke_T, format = 'json')
        self.assertEqual(201, response.status_code)

    def test_Get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class Nuke_Tests(APITestCase):

    url = '/api/nuke/'

    def setUp(self):

        self.nps_name = "Нововоронежская"
        self.country = "Россия"
        self.factor = 1

        self.nuke, created = NukeList.objects.get_or_create(
            nps_name = self.nps_name,
            country = self.country,
            factor = self.factor
        )


    def test_Get_One(self):
        print(self.nuke.uuid)
        uuid_T = self.nuke.uuid
        response = self.client.get(self.url + f'{uuid_T}')
        self.assertEqual(200, response.status_code)


    def test_Patch(self):

        self.nuke, created = NukeList.objects.get_or_create(
            nps_name = self.nps_name,
            country = self.country,
            factor = self.factor
        )

        uuid_T = self.nuke.uuid

        nuke_P = {
            'nps_name' : self.nps_name,
            'country' : self.country,
            'factor' : self.factor
        }

        response = self.client.patch(self.url + f'{uuid_T}', data = nuke_P, format = 'json')

        self.assertEqual(202, response.status_code)

    def test_Delete(self):

        uuid_T = self.nuke.uuid
        response = self.client.delete(self.url + f'{uuid_T}')
        self.assertEqual(204, response.status_code)
