import requests
from rest_framework.views import APIView, Response
from uuid import UUID
import logging
from .baseview import BaseView
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException

from ..permissions import IsAuthenticatedByAuthenticateService

EMPCB = CircuitBreaker(
    failure_threshold = 5,
    recovery_timeout = 30,
    expected_exception = RequestException
)



class Emp(BaseView):
    permission_classes = (IsAuthenticatedByAuthenticateService, )


    URL_EMP = "'http://localhost:8004/api/person/'"



    def __init__(self):
        pass

    @EMPCB
    def get_emp(self,request,emp_uuid):

        self.info(request)
        response_emp = requests.get(self.URL_EMP + f'{emp_uuid}')
        emp = self.safeResponse(response_emp)
        return Response(emp, status = response_emp.status_code)
    
    @EMPCB
    def patch_emp(self, request, emp_uuid):

        self.info(request)
        response = request.patch(self.URL_EMP + f'{emp_uuid}')
        mode_emp = self.safeResponse(response)
        return Response(mode_emp, status = response.status_code)
    
    @EMPCB
    def delete_emp(self, request, emp_uuid):
        
        self.info(request)
        response = requests.delete(self.URL_EMP + f'{emp_uuid}')
        del_emp = self.safeResponse(response)
        return Response(del_emp, status = response.status_code)
        