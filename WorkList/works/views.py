from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView, Request, Response
from logging import Logger
from uuid import UUID
from .serializers import work_Serializer, AppAuthSerializer
from .models import WorkList, CustomToken
from .permission import IsAuthenticatedByToken
from .authentication import ExpiringTokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from django.core.exceptions import FieldError
import logging
from sys import stdout
from rest_framework.authtoken.views import ObtainAuthToken

DEFAULT_PAGE_LIMIT = settings.DEFAULT_PAGE_LIMIT

class BaseView(APIView):
    authentication_classes = (ExpiringTokenAuthentication, )
    permission_classes = (IsAuthenticatedByToken, )
    logger = logging.getLogger(name='views')
    formatter = '{method} : {url} : {content_type} : {msg}'

    def info(self, request: Request, msg: str = None) -> None:
        self.logger.info(
            self.formatter.format(
                method=request.method,
                url=request._request.get_raw_uri(),
                content_type=request.content_type,
                msg=msg
            )
        )

class Work(BaseView):

    def get(self, request, w_uuid: UUID):

        self.info(request)

        try:
            work_R = WorkList.objects.get(pk = w_uuid)
        except WorkList.DoesNotExist as error:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = work_Serializer(instance = work_R)
        return Response(serializer.data)


    def delete(self, request, w_uuid: UUID):

        self.info(request)

        try:
            Work_R = WorkList.objects.get(pk = w_uuid)
        except WorkList.DoesNotExist as error:
            return Response(status = status.HTTP_404_NOT_FOUND)
        Work_R.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def patch(self, request, w_uuid: UUID):

            self.info(request)

            try:
                Work_R = WorkList.objects.get(pk = w_uuid)
            except WorkList.DoesNotExist as error:
                return Response(status = status.HTTP_404_NOT_FOUND)
            serializer = work_Serializer(instance = Work_R, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(data = serializer.data, status = status.HTTP_202_ACCEPTED)
            return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Works(BaseView):

    def __clear_request_params(self, request: Request) -> dict:
            params = request.query_params.dict()

            if 'page' in params: params.pop('page')
            #if 'offset' in params: params.pop('offset')

            return params

    def get(self, request):

        self.info(request)
        params = self.__clear_request_params(request)
        
        try:
            Works_R = WorkList.objects.filter(**params)

        except FieldError as error:
            return Response(status = status.HTTP_400_BAD_REQUEST )

        paginator = PageNumberPagination()
        paginator.default_limit = DEFAULT_PAGE_LIMIT
        page = paginator.paginate_queryset(Works_R, request)

        serializer = work_Serializer(Works_R, many = True)
        return Response(data = serializer.data)

    def post(self, request):

        self.info(request)

        serializer = work_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)

        return Response(status = status.HTTP_400_BAD_REQUEST)


class CustomObtainTokenView(BaseView, ObtainAuthToken):
    permission_classes = []
    authentication_classes = []
    serializer_class = AppAuthSerializer
    def post(self, request: Request) -> Response:
        self.info(request)
        
        serializer = self.serializer_class(data = request.data, context = {'request': request})
        serializer.is_valid(raise_exception = True)
        token = CustomToken.objects.create()

        return Response(data = {'token': token.token}, status = status.HTTP_200_OK)
