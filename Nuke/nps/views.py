from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView, Request, Response
from logging import Logger
from uuid import UUID
from .serializers import nuke_Serializer, ToDoUserSerializer
from .models import NukeList
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from django.core.exceptions import FieldError
import logging
from sys import stdout
from rest_framework.permissions import IsAuthenticated
# Create your views here.
DEFAULT_PAGE_LIMIT = settings.DEFAULT_PAGE_LIMIT

class BaseView(APIView):
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

    def exception(self, request: Request, msg: str = None) -> None:
        self.logger.exception(
            self.formatter.format(
                method=request.method,
                url=request._request.get_raw_uri(),
                content_type=request.content_type,
                msg=msg
            )
        )

"""

class Nuke(BaseView):

    def get(self, request, n_uuid: UUID):

        self.info(request)

        try:
            nuke_R = NukeList.objects.get(pk = n_uuid)
        except NukeList.DoesNotExist as error:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = nuke_Serializer(instance = nuke_R)
        return Response(serializer.data)


    def delete(self, request, n_uuid: UUID):

        self.info(request)

        try:
            nuke_R = NukeList.objects.get(pk = n_uuid)
        except NukeList.DoesNotExist as error:
            return Response(status = status.HTTP_404_NOT_FOUND)
        nuke_R.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def patch(self, request, n_uuid: UUID):

            self.info(request)

            try:
                nuke_R = NukeList.objects.get(pk = n_uuid)
            except NukeList.DoesNotExist as error:
                return Response(status = status.HTTP_404_NOT_FOUND)
            serializer = nuke_Serializer(instance = nuke_R, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(data = serializer.data, status = status.HTTP_202_ACCEPTED)
            return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Nukes(BaseView):

    def __clear_request_params(self, request: Request) -> dict:
            params = request.query_params.dict()

            if 'page' in params: params.pop('page')

            return params

    def get(self, request):

        self.info(request)

        try:
            nukes_R = NukeList.objects.filter()

        except FieldError as error:
            return Response(status = status.HTTP_400_BAD_REQUEST )

        paginator = PageNumberPagination()
        paginator.default_limit = DEFAULT_PAGE_LIMIT
        page = paginator.paginate_queryset(nukes_R, request)

        serializer = nuke_Serializer(nukes_R, many = True)
        return Response(data = serializer.data)

    def post(self, request):

        self.info(request)

        serializer = nuke_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)

        return Response(status = status.HTTP_400_BAD_REQUEST)

        """

class UserInfoView(BaseView):
    permission_classes = (IsAuthenticated, )
    serializer = ToDoUserSerializer
    def get(self, request: Request, format: str = 'json') -> Response:
        self.info(request, request.user)

        if request.user is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer(instance = request.user)

        return Response(data = serializer.data, status = status.HTTP_200_OK)

