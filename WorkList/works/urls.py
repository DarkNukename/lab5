from django.urls import path
from .views import *
urlpatterns = [
    path('works/', Works.as_view()),
    path('work/<uuid:w_uuid>', Work.as_view()),
    path('auth/', CustomObtainTokenView.as_view())
]
