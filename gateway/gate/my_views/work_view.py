from gate.my_requests.work_requests import Work
import requests
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from uuid import UUID
import logging
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException

class Work_View(Work):
    #permission_classes = (IsAuthenticated,) # напсать

    def __init__(self):
        pass
    
    def get(self, request, work_uuid):
        
        try:
            response = self.get_work(request, work_uuid)
            work = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

       
        return Response(work, status = code)


    def patch(self, request, work_uuid):
        
        try:
            response = self.patch_work(request, work_uuid)
            work = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

        
        return Response(work, status = code)


    def delete(self, request, work_uuid):

        try:
            response = self.delete_work(request, work_uuid)
            work = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

        
        return Response(work, status = code)