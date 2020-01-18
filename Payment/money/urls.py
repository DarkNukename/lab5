from django.urls import path
from .views import *
urlpatterns = [
    path('payments/', Moneys.as_view()),
    path('payment/<uuid:p_uuid>', Money.as_view()),
]
