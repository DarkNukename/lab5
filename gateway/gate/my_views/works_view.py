from gate.my_requests.works_requests import Works
import requests
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from uuid import UUID
import logging
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException




class Works_View(Works):

    #permission_classes = (IsAuthenticated,) # напсать

    def __init__(self):
        pass

    def get(self, request):
        
        try:
            work, code = self.get_works(request)

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")

        return Response(work , status = code)


    def post(self, request):
        
        try:
            response = self.post_work(request)
            work = response.data
            code = response.status_code

        except CircuitBreakerError:
            return Response(status = "500 Internal Server Error")


        return Response(work, status = code)
