import requests
from rest_framework.views import APIView, Response
from uuid import UUID
import logging
from .baseview import BaseView
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException
from ..decorators import TokenHeader
from ..permissions import IsAuthenticatedByAuthenticateService
from django.conf import settings
from django.core.cache import cache


WORKSCB = CircuitBreaker(
    failure_threshold = 5,
    recovery_timeout = 30,
     expected_exception = RequestException
)


Tokens = TokenHeader(
    url = 'http://localhost:8002/api/auth/',
    cache = cache ,
    app_id = settings.EMP_ID,
    app_secret = settings.EMP_SECRET,
    t_label = 'emp'
)


class Works(BaseView):
    
    URL_WORKS = 'http://localhost:8002/api/works/'

    @WORKSCB
    @Tokens
    def get_works(self,request, headers = {}):
        self.info(request)
        query = "?"
        params = request.query_params.dict()
        query += '&'.join([f"{key}={params[key]}" for key in params])
        response_works = requests.get(self.URL_WORKS + query, headers = headers)
        works = self.safeResponse(response_works)
        
        return (works, response_works.status_code)

    @WORKSCB
    def post_work(self, request):
        self.info(request)
        response = requests.post(self.URL_WORKS, request.data)
        new_work = self.safeResponse(response)
        return Response(new_work, status = response.status_code)