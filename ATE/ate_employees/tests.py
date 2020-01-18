from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, force_authenticate, APITestCase
from .models import ATE_Employees
import json


class Persons_Tests(APITestCase):

    url = '/api/persons/'

    def test_Post(self):

        person_T = {
            'first_name': 'Евгиний',
            'second_name': 'Евтушенко',
            'english_level': '1',
            'specialization': "1",
            'skill': "1",
            'work': 0
            }

        response = self.client.post(self.url, person_T, format = 'json')
        self.assertEqual(201, response.status_code)

    def test_Get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class Person_Tests(APITestCase):

    url = '/api/person/'

    def setUp(self):

        self.first_name = "Евгений"
        self.second_name = "Евтушенко"
        self.english_level = "1"
        self.specialization = '1'
        self.skill = "1"
        self.work = 0

        self.person, created = ATE_Employees.objects.get_or_create(
            first_name = self.first_name,
            second_name = self.second_name,
            english_level = self.english_level,
            specialization = self.specialization,
            skill = self.skill,
            work = self.work
        )


    def test_Get_One(self):
        print(self.person.uuid)
        uuid_T = self.person.uuid
        response = self.client.get(self.url + f'{uuid_T}')
        self.assertEqual(200, response.status_code)


    def test_Patch(self):

        self.person, created = ATE_Employees.objects.get_or_create(
            first_name = self.first_name,
            second_name = self.second_name,
            english_level = self.english_level,
            specialization = self.specialization,
            skill = self.skill,
            work = self.work
        )

        uuid_T = self.person.uuid

        person_P = {
            'first_name' : self.first_name,
            'second_name' : self.second_name,
            'english_level' : "3",
            'specialization' : "2",
            'skill' : "4",
            'work' : self.work
        }

        response = self.client.patch(self.url + f'{uuid_T}', data = person_P, format = 'json')

        self.assertEqual(202, response.status_code)

    def test_Delete(self):

        uuid_T = self.person.uuid
        response = self.client.delete(self.url + f'{uuid_T}')
        self.assertEqual(204, response.status_code)
