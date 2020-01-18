from django.shortcuts import render
from rest_framework.views import APIView, Response
from uuid import UUID
import requests
import logging
#import celeryQue.tasks as ts
from circuitbreaker import CircuitBreaker, CircuitBreakerError
from requests.exceptions import RequestException

from .permissions import IsAuthenticatedByAuthenticateService

 #ts.post.delay()

class BaseView(APIView):
    logger = logging.getLogger(name = 'views')
    formatter = '{method} : {url} : {content_type} : {msg}'

    def info(self, request, msg = None):
        self.logger.info(
            self.formatter.format(
                method=request.method,
                url=request._request.get_raw_uri(),
                content_type=request.content_type,
                msg=msg
            )
        )

    def exception(self, request, msg = None):
        self.logger.exception(
            self.formatter.format(
                method=request.method,
                url=request._request.get_raw_uri(),
                content_type=request.content_type,
                msg=msg
            )
        )
    def safeResponse(self,response):
        try:
            return response.json()
           

        except ValueError as error:
            #self.exception()
            return response.text

NukesCB = CircuitBreaker(
    failure_threshold=5,
    recovery_timeout=30,
    expected_exception=RequestException
)

class NukesView(BaseView):
    
    URL = 'http://localhost:8001/api/nukes/'

    def get(self,request):

    
        #def f1(request):
        #    pass
        


        self.info(request)
        query = "?"
        params = request.query_params.dict()
        query += '&'.join([f"{key}={params[key]}" for key in params])
        response = requests.get(self.URL + query)
        #ts.post.delay()

       #try:
        #    f1()

        #except (CircuitBreakerError, RequestException) as error:
          #  pass"""

        return Response(self.safeResponse(response), status = response.status_code)

    def post(self, request):
        self.info(request)
        response = requests.post(self.URL, request.data)
        return Response(self.safeResponse(response), status = response.status_code)

class NukeView(BaseView):

    URL = 'http://localhost:8001/api/nuke/'

    def get(self,request,n_uuid):
        self.info(request)
        response = requests.get(self.URL + f'{n_uuid}')
        return Response(self.safeResponse(response), status = response.status_code)

    def patch(self, request, n_uuid):
        self.info(request)
        response = requests.patch(self.URL + f'{n_uuid}', request.data)
        return Response(self.safeResponse(response), status = response.status_code)

    def delete(self, request, n_uuid):
        self.info(request)
        response = requests.delete(self.URL + f'{n_uuid}')
        return Response(self.safeResponse(response), status = response.status_code)

# Оно работает. Будьте терпеливы, у меня аутизм

class WorksView(BaseView):
    
    URL = 'http://localhost:8002/api/works/'

    def get(self,request):
        self.info(request)
        query = "?"
        params = request.query_params.dict()
        query += '&'.join([f"{key}={params[key]}" for key in params])
        response = requests.get(self.URL + query)
     
        return Response(self.safeResponse(response), status = response.status_code)


    def post(self, request):
        self.info(request)
        response = requests.post(self.URL, request.data)
        return Response(self.safeResponse(response), status = response.status_code)
        
class WorkView(BaseView):

    URL = 'http://localhost:8002/api/work/'
    URL1 = 'http://localhost:8004/api/persons/'
    URL2 = 'http://localhost:8004/api/person/'

    def get(self,request,w_uuid):
        self.info(request)
        response = requests.get(self.URL + f'{w_uuid}')
        print(response)
        return Response(self.safeResponse(response), status = response.status_code)

    def patch(self, request, w_uuid):
        self.info(request)
        response = requests.patch(self.URL + f'{w_uuid}', request.data)
        return Response(self.safeResponse(response), status = response.status_code)

    def delete(self, request, w_uuid):
        self.info(request)

        respons_1 = requests.get(self.URL1 + f'?work={w_uuid}')
        #if response.status_code != 200:
            #errors

        persons = self.safeResponse(response_1)

        for person in persons:
            uuid_ = person['uuid']
            response_2 = requests.patch(self.URL2 + f'{uuid_}', data = {'work' : UUID(int = 0)})

            #if response_.status_code != 202:
                #errors

        try:
            response = requests.delete(self.URL + f'{w_uuid}')
        except:
            persons = response_2.json()
            for person in persons:
                uuid_ = person['uuid']
                response = requests.patch(self.URL2 + f'{uuid_}', data = {'work' : w_uuid})
            return Response(self.safeResponse(response), status = response.status_code)

        return Response(self.safeResponse(response), status = response.status_code)

class PaymentsView(BaseView):

    URL = 'http://localhost:8003/api/payments/'

    def get(self,request):
        self.info(request)
        query = "?"
        params = request.query_params.dict()
        query += '&'.join([f"{key}={params[key]}" for key in params])
        response = requests.get(self.URL + query)
        return Response(self.safeResponse(response), status = response.status_code)

    def post(self, request):
        self.info(request)
        response = requests.post(self.URL, request.data)
        return Response(self.safeResponse(response), status = response.status_code)

class PaymentView(BaseView):

        URL = 'http://localhost:8003/api/payment/'

        def get(self,request,p_uuid):
            self.info(request)
            response = requests.get(self.URL + f'{p_uuid}')
            return Response(self.safeResponse(response), status = response.status_code)

        def patch(self, request, p_uuid):
            self.info(request)
            response = requests.patch(self.URL + f'{p_uuid}', request.data)
            return Response(self.safeResponse(response), status = response.status_code)

        def delete(self, request, p_uuid):
            self.info(request)
            response = requests.delete(self.URL + f'{p_uuid}')
            return Response(self.safeResponse(response), status = response.status_code)

class PersonsView(BaseView):
    URL = 'http://localhost:8004/api/persons/'
    URL_1 = 'http://localhost:8003/api/payments/'

    def get(self,request):
        self.info(request)
        query = "?"
        params = request.query_params.dict()
        query += '&'.join([f"{key}={params[key]}" for key in params])
        #response = requests.get(self.URL + query)
        
        response_1 = requests.get(self.URL + query)
        _r = response_1.json()

        try:
            response_2 = requests.get(self.URL_1)
        except:
            for i in _r:
                i['salary'] = "Нет Данных"
            return Response(_r, status = response_1.status_code)
        
        _s = response_2.json()

        for i in _r:
            for j in _s:
                if i['skill'] == j['skill'] and i['specialization'] == j['specialization']:
                    i['salary'] = j['coeff']
        print(_r)

        

        return Response(_r, status = response_1.status_code)

    def post(self, request):
        self.info(request)
        response = requests.post(self.URL, request.data)
        return Response(self.safeResponse(response), status = response.status_code)

class PersonView(BaseView):
    URL = 'http://localhost:8004/api/person/'

    def get(self,request,p_uuid):
        self.info(request)
        response = requests.get(self.URL + f'{p_uuid}')
        return Response(self.safeResponse(response), status = response.status_code)

    def patch(self, request, p_uuid):
        self.info(request)
        response = requests.patch(self.URL + f'{p_uuid}', request.data)
        return Response(self.safeResponse(response), status = response.status_code)

    def delete(self, request, p_uuid):
        self.info(request)
        response = requests.delete(self.URL + f'{p_uuid}')
        return Response(self.safeResponse(response), status = response.status_code)
"""
class Cost_Money(BaseView):

    URL = 'http://localhost:8002/api/work/'
    URL1 = 'http://localhost:8003/api/payments/'
    URL2 = 'http://localhost:8004/api/person/'
    URL3 = 'http://localhost:8001/api/nukes/'

    def get(self, request, p_uuid):

        self.info(request)

        response_1 = requests.get(self.URL2 + f'{p_uuid}')
        person_ = self.safeResponse(response_1)
        w_uuid =person_['work']
        w_skill = person_['skill']
        w_specialization = person_['specialization']
        

        response_1 = requests.get(self.URL1 + f'?skill={w_skill}&specialization={w_specialization}')
        cost_ = self.safeResponse(response_1)
        cost = cost_[0]
        cost = cost['coeff']
        print(cost)

        response_1 = requests.get(self.URL + f'{w_uuid}')
        work_ = self.safeResponse(response_1)
        nps = work_['nps_name']

        response_1 = requests.get(self.URL3 + f'?nps_name={nps}')
        nps_ = self.safeResponse(response_1)
        fact = nps_[0]
        fact = fact['factor']
        print(int(cost) * int(fact))

        response = {"money" : int(cost) * int(fact)}
        res = json.dumps(response,
                 sort_keys=True, indent=4, separators=(',', ': '))
        return Response(self.safeResponse(response), status = response.status_code)

        """