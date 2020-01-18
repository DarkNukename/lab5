from gate.my_requests.pays_requests import Pays
import requests
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from uuid import UUID
import logging
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException

class Pays_View(Pays):

    #permission_classes = (IsAuthenticated,) # напсать

    def __init__(self):
        pass
    
    def get(self, request):
        
        try:
            response = self.get_pays(request)
            pays = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")


        
        return Response(pays, status = code)


    def post(self, request):
        
        try:
            response = self.post_pay(request)

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

        pay = response.data
        code = response.status_code

        return Response(pay, status = code)