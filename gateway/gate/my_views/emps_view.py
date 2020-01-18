from gate.my_requests.emps_requests import Emps
import requests
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from uuid import UUID
import logging
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException

class Emps_View(Emps):

    #permission_classes = (IsAuthenticated,) # напсать

    def __init__(self):
        pass
    
    def get(self, request):
        
        try:
            response = self.get_emps(request)
            emps = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = 500)


        
        return Response(emps, status = code)


    def post(self, request):
        
        try:
            response = self.post_emp(request)
            emp = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = 500)

        
        return Response(emp, status = code)
