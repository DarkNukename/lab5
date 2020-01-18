import requests
from rest_framework.views import APIView, Response
from uuid import UUID
import logging
from .baseview import BaseView
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException

PAYSCB = CircuitBreaker(
    failure_threshold = 5,
    recovery_timeout = 30,
     expected_exception = RequestException
)

class Pays(BaseView):

    URL_PAYS= 'http://localhost:8003/api/payments/'

    @PAYSCB
    def get_pays(self,request):
        self.info(request)
        query = "?"
        params = request.query_params.dict()
        query += '&'.join([f"{key}={params[key]}" for key in params])
        response = requests.get(self.URL_PAYS + query)
        pays = self.safeResponse(response)
        return Response(pays, status = response.status_code)

    @PAYSCB
    def post_pay(self, request):
        self.info(request)
        response = requests.post(self.URL_PAYS, request.data)
        return Response(self.safeResponse(response), status = response.status_code)