from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView, Request, Response
from logging import Logger
from uuid import UUID
from .serializers import Pay_Serializer
from .models import PayList
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from django.core.exceptions import FieldError
import logging
from sys import stdout

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

class Money(BaseView):

    def get(self, request, p_uuid: UUID):

        self.info(request)

        try:
            moneys_R = PayList.objects.get(pk = p_uuid)
        except PayList.DoesNotExist as error:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = Pay_Serializer(instance = moneys_R)
        return Response(serializer.data)


    def delete(self, request, p_uuid: UUID):

        self.info(request)

        try:
            moneys_R = PayList.objects.get(pk = p_uuid)
        except PayList.DoesNotExist as error:
            return Response(status = status.HTTP_404_NOT_FOUND)
        moneys_R.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def patch(self, request, p_uuid: UUID):

            self.info(request)

            try:
                moneys_R = PayList.objects.get(pk = p_uuid)
            except PayList.DoesNotExist as error:
                return Response(status = status.HTTP_404_NOT_FOUND)
            serializer = Pay_Serializer(instance = moneys_R, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(data = serializer.data, status = status.HTTP_202_ACCEPTED)
            return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Moneys(BaseView):

    def get(self, request):

        self.info(request)

        try:
            money_R = PayList.objects.filter()

        except FieldError as error:
            return Response(status = status.HTTP_400_BAD_REQUEST )

        paginator = PageNumberPagination()
        paginator.default_limit = DEFAULT_PAGE_LIMIT
        page = paginator.paginate_queryset(money_R, request)

        serializer = Pay_Serializer(money_R, many = True)
        return Response(data = serializer.data)

    def post(self, request):

        self.info(request)

        serializer = Pay_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)

        return Response(status = status.HTTP_400_BAD_REQUEST)
