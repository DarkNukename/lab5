import requests
from rest_framework.views import APIView, Response
from uuid import UUID
import logging
from .baseview import BaseView
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException


PAYCB = CircuitBreaker(
    failure_threshold = 5,
    recovery_timeout = 30,
     expected_exception = RequestException
)


class Pay(BaseView):

        URL_PAY = 'http://localhost:8003/api/payment/'


        @PAYCB
        def get_pay(self,request, pay_uuid):
            self.info(request)
            response = requests.get(self.URL_PAY + f'{pay_uuid}')
            return Response(self.safeResponse(response), status = response.status_code)

        @PAYCB
        def patch_pay(self, request, pay_uuid):
            self.info(request)
            response = requests.patch(self.URL_PAY + f'{pay_uuid}', request.data)
            return Response(self.safeResponse(response), status = response.status_code)

        @PAYCB
        def delete_pay(self, request, pay_uuid):
            self.info(request)
            response = requests.delete(self.URL_PAY + f'{pay_uuid}')
            return Response(self.safeResponse(response), status = response.status_code)
