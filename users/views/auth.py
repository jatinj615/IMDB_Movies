from django.contrib.auth import get_user_model, authenticate, login, logout
from users.serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, generics
from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.views import ObtainAuthToken



class CreateUserView(generics.CreateAPIView):
    """
    Registration for new User
    """
    model = get_user_model()
    permission_classes = [permissions.AllowAny]

    serializer_class = UserSerializer

    

class LoginView(APIView):
    """
    User Login and auth token Generation
    """
    def post(self, request, *args, **kwargs):
        user = authenticate(username=self.request.data['username'], password=self.request.data['password'])
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            response_data = {'token': token.key}
            return Response(response_data, status=HTTP_200_OK)
        else:
            return Response(status=404)

