import requests
from rest_framework.views import APIView, Response
from uuid import UUID
import logging
from .baseview import BaseView
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException

WORKCB = CircuitBreaker(
    failure_threshold = 5,
    recovery_timeout = 30,
     expected_exception = RequestException
)

class Work(BaseView):

    URL_WORK = 'http://localhost:8002/api/work/'
    URL_EMPS = 'http://localhost:8004/api/persons/'
    URL_EMP = 'http://localhost:8004/api/person/'
    
    @WORKCB
    def get_work(self,request,work_uuid):
        self.info(request)
        response = requests.get(self.URL_WORK + f'{work_uuid}')
        #print(response)
        return Response(self.safeResponse(response), status = response.status_code)

    @WORKCB
    def patch_work(self, request, work_uuid):
        self.info(request)
        response = requests.patch(self.URL_WORK + f'{work_uuid}', request.data)
        return Response(self.safeResponse(response), status = response.status_code)

    @WORKCB
    def delete_work(self, request, work_uuid):
        self.info(request)

        response_emps = requests.get(self.URL_EMPS + f'?work={work_uuid}')
        #if response.status_code != 200:
            #errors

        persons = self.safeResponse(response_emps)

        for person in persons:
            uuid_ = person['uuid']
            response_emps_patch = requests.patch(self.URL_EMP + f'{uuid_}', data = {'work' : UUID(int = 0)})

            #if response_.status_code != 202:
                #errors

        
        response = requests.delete(self.URL_WORK + f'{work_uuid}')
        
        return Response(self.safeResponse(response), status = response.status_code)