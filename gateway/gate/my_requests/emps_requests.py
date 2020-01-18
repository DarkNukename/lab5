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

EMPSCB = CircuitBreaker(
    failure_threshold = 5,
    recovery_timeout = 30,
     expected_exception = RequestException
)

Tokens = TokenHeader(
    url = 'http://localhost:8004/api/persons/',
    cache = cache ,
    app_id = settings.EMP_ID,
    app_secret = settings.EMP_SECRET,
    t_label = 'emp'
)


class Emps(BaseView):

    URL_EMPS = 'http://localhost:8004/api/persons/'
    URL_PAYS = 'http://localhost:8003/api/payments/'

    permission_classes = (IsAuthenticatedByAuthenticateService, )

    @EMPSCB
    @Tokens
    def get_emps(self, request):

        self.info(request)

        query = "?"
        params = request.query_params.dict()
        query += '&'.join([f"{key}={params[key]}" for key in params])
        
        response_emps = requests.get(self.URL_EMPS + query)
        emps = self.safeResponse(response_emps)

        try:
            response_pays = requests.get(self.URL_PAYS)
        except:
            for emp in emps:
                emp['salary'] = "Нет Данных"
            return Response(emps, status = response_emps.status_code)
        
        pays = self.safeResponse(response_pays)

        for emp in emps:

            fileIsFind = False

            for pay in pays:
                if (emp['skill'] == pay['skill'] and 
                    emp['specialization'] == pay['specialization']):

                    emp['salary'] = pay['coeff']
                    fileIsFind = True
                    break

            if fileIsFind == False:
                emp['salary'] = "Нет Данных"

        return Response(emps, status =  response_emps.status_code)

    @EMPSCB
    def post_emp(self, request):

        self.info(request)
        response = requests.post(self.URL_EMPS, request.data)
        new_emp = response.safeResponse()
        return Response(new_emp, status = response.status_code)

