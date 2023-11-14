from .models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from.serializers import UserSerializer
from utils.common import success_response, error_response
from construction_manager import settings
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class CreateUser(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        try:
            user = self.serializer_class(data=request.data)
            if user.is_valid():
                user.save()
                return success_response(message="User created successfully!")
            return error_response(message="Invalid Data")
        except Exception as e:
            return error_response(message=str(e))
        
class LoginUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            username = request.data.get("username", None)
            password = request.data.get("password", None)
            user = authenticate(username=username, password=password)
            if user is not None:
                user = User.objects.get(username=username)
                response_data = {
                    'username': user.username,
                    'refresh': user.tokens()['refresh'],
                    'access': user.tokens()['access'],
                    "access_expires_in": str(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]),
                    "refresh_expires_in": str(settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"])
                }
                return success_response(data=response_data, message="User logged in Successfully!")
            else:
                return error_response(message="Invalid Credentials")
        except Exception as e:
            return error_response(message=str(e))
        
class GetUsers(APIView):
    serializer_class = UserSerializer
    def get(self, request):
        try:
            user = User.objects.all()
            serializer_data = self.serializer_class(user, many=True).data
            return success_response(data=serializer_data)
        except Exception as e:
            return error_response(message=str(e))


class Logout(APIView):
    def post(self, request):
        try:
            token = request.data.get('refresh')
            tc  = RefreshToken(token)
            tc.blacklist()
            return success_response(message="Logged out Successfully")
        except Exception as e:
            return error_response(message=str(e))