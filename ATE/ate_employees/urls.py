from django.urls import path
from .views import *
urlpatterns = [
    path('persons/', Persons.as_view()),
    path('person/<uuid:p_uuid>', Person.as_view()),
]
