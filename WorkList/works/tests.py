from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, force_authenticate, APITestCase
from .models import WorkList
import json


class Works_Tests(APITestCase):

    url = '/api/works/'

    def test_Post(self):

        work_T = {
            'nps_name': 'Нововоронежская',
            'english_level': '1',
            'specialization': "1",
            'skill': "1",
            'sum': 0
            }

        response = self.client.post(self.url, work_T, format = 'json')
        self.assertEqual(201, response.status_code)

    def test_Get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class Work_Tests(APITestCase):

    url = '/api/work/'

    def setUp(self):

        self.nps_name = "Нововоронежская"
        self.english_level = "1"
        self.specialization = '1'
        self.skill = "1"
        self.sum = 1

        self.work, created = WorkList.objects.get_or_create(
            nps_name = self.nps_name,
            english_level = self.english_level,
            specialization = self.specialization,
            skill = self.skill,
            sum = self.sum
        )


    def test_Get_One(self):

        uuid_T = self.work.uuid
        response = self.client.get(self.url + f'{uuid_T}')
        self.assertEqual(200, response.status_code)


    def test_Patch(self):

        self.work, created = WorkList.objects.get_or_create(
            nps_name = self.nps_name,
            english_level = self.english_level,
            specialization = self.specialization,
            skill = self.skill,
            sum = self.sum
        )

        uuid_T = self.work.uuid

        work_P = {
            'nps_name' : self.nps_name,
            'english_level' : "3",
            'specialization' : "2",
            'skill' : "4",
            'sum' : self.sum
        }

        response = self.client.patch(self.url + f'{uuid_T}', data = work_P, format = 'json')

        self.assertEqual(202, response.status_code)

    def test_Delete(self):

        uuid_T = self.work.uuid
        response = self.client.delete(self.url + f'{uuid_T}')
        self.assertEqual(204, response.status_code)
