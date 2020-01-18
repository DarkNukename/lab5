from django.urls import path
from .views import UserInfoView
urlpatterns = [
    #path('nukes/', Nukes.as_view()),
    #path('nuke/<uuid:n_uuid>', Nuke.as_view()),

    path('users/info/', UserInfoView.as_view(), name = 'user-info'),
]
