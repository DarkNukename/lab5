"""Nuke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('nps.urls')),
    path('o2/', include('oauth2_provider.urls', namespace='oauth2_provider')), #!
    path('accounts/', include('django.contrib.auth.urls')),
]

"""

Гейтвей




def info(self, request: Request) -> Tuple[Dict, int]:
        response = self.get(
            url = self.URL + self.TOKENS['info'],
            headers = self.authenticate_header(request),
        )

        return self._process_response(response = response, task_name = 'INFO')

class IsAuthenticatedByAuthenticateService(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        token = request.META.get('HTTP_AUTHORIZATION')  - вытащит токен
        if token:
            _, code = UserRequester().info(request = request)
        return code == 200

_________________________________________________________________


nuke по какому-то url

def get(self, request: Request, format: str = 'json') -> Response:
        self.info(request, request.user)

        if request.user is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)

        serializer = CustomUserSerializer(instance = request.user)

        return Response(data = serializer.data, status = status.HTTP_200_OK)

"""
