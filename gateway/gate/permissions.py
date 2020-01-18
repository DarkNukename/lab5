from rest_framework.permissions import BasePermission
import requests
# token = request.META.get('HTTP_AUTHORIZATION')
# headers = {'Authorization': request.META.get('HTTP_AUTHORIZATION')}

class IsAuthenticatedByAuthenticateService(BasePermission):

    def has_permission(self, request, view) -> bool:
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            return False
        
        response = self.info(request = request)
        return response.status_code == 200

    def info(self, request):

        URL = "http://localhost:8085/api/users/info/"
        response = requests.get(
            url = URL,
            headers = {'Authorization': request.META.get('HTTP_AUTHORIZATION')},
        )
        return response