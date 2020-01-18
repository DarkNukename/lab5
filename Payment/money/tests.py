from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, force_authenticate, APITestCase
from .models import PayList
import json

# Create your tests here.
class Moneys_Tests(APITestCase):

    url = '/api/payments/'

    def test_Post(self):

        pay_T = {
            'skill': '1',
            'specialization': '1',
            'coeff': 1
            }

        response = self.client.post(self.url, pay_T, format = 'json')
        self.assertEqual(201, response.status_code)

    def test_Get(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class Money_Tests(APITestCase):

    url = '/api/payment/'

    def setUp(self):

        self.skill = "1"
        self.specialization = "1"
        self.coeff = 1

        self.pay, created = PayList.objects.get_or_create(
            skill = self.skill,
            specialization = self.specialization,
            coeff = self.coeff
        )


    def test_Get_One(self):
        print(self.pay.uuid)
        uuid_T = self.pay.uuid
        response = self.client.get(self.url + f'{uuid_T}')
        self.assertEqual(200, response.status_code)


    def test_Patch(self):

        self.pay, created = PayList.objects.get_or_create(
            skill = self.skill,
            specialization = self.specialization,
            coeff = self.coeff
        )

        uuid_T = self.pay.uuid

        pay_P = {
            'skill' : "2",
            'specialization' : "2",
            'coeff' : "2"
        }

        response = self.client.patch(self.url + f'{uuid_T}', data = pay_P, format = 'json')

        self.assertEqual(202, response.status_code)

    def test_Delete(self):

        uuid_T = self.pay.uuid
        response = self.client.delete(self.url + f'{uuid_T}')
        self.assertEqual(204, response.status_code)
