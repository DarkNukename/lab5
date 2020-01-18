from gate.my_requests.emp_requests import Emp
import requests
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from uuid import UUID
import logging
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException

class Emp_View(Emp):
    #permission_classes = (IsAuthenticated,) # напсать

    def __init__(self):
        pass
    
    def get(self, request, emp_uuid):
        
        try:
            response = self.get_emp(request, emp_uuid)
            emp = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

        # if response.is

        
        return Response(emp, status = code)


    def patch(self, request, emp_uuid):
        
        try:
            response = self.patch_emp(request, emp_uuid)
            emp = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

        
        return Response(emp, status = code)


    def delete(self, request, emp_uuid):

        try:
            response = self.delete_emp(request, emp_uuid)
            emp = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

        
        return Response(emp, status = code)
