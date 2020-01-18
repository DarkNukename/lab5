from gate.my_requests.pay_requests import Pay
import requests
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from uuid import UUID
import logging
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException

class Pay_View(Pay):
    #permission_classes = (IsAuthenticated,) # напсать

    def __init__(self):
        pass
    
    def get(self, request, pay_uuid):
        
        try:
            response = self.get_pay(request, pay_uuid)

            pay = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")


        
        return Response(pay, status = code)


    def patch(self, request, pay_uuid):
        
        try:
            response = self.patch_pay(request, pay_uuid)

            pay = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

        
        return Response(pay, status = code)


    def delete(self, request, pay_uuid):

        try:
            response = self.delete_pay(request, pay_uuid)

            pay = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

        
        return Response(pay, status = code)
