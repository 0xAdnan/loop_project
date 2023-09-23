from django.shortcuts import render
from rest_framework.views import APIView

from lms.libs.constant.constants import JWT
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .models import UserData
import jwt, datetime
from django.contrib.auth.models import update_last_login

from .libs.redis.redis import MasterRedis
from .libs.Constants.constants import UserConstant
# from .users.libs.Authentication.auth import authentication
from .libs.Authentication.auth import authentication
from django.forms.models import model_to_dict


# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        redis = MasterRedis()

        email = request.data['email']
        password = request.data['password']

        user = UserData.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User Not Found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=72),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, JWT.JWT_SECRET, algorithm='HS256')
        update_last_login(None, user)
        key = str(user.id) + UserConstant.REDIS_USER_KEY

        redis.set_keys(key, token)
        response = Response()
        response.data = {'message': 'Successfully Logged In',
                         'jwt': token
                         }
        return response


class UserView(APIView):

    @authentication
    def get(self, request):

        headers = request.headers
        response = Response()
        token = headers.get("Authorization")
        payload = jwt.decode(token, JWT.JWT_SECRET, algorithms=['HS256'])


        user = UserData.objects.filter(id=payload['id']).first()

        serializer = UserSerializer(user)
        if user:
            response.data = {
                "message": serializer.data,
                "status": status.HTTP_200_OK
            }
            return response
        else:

            response.data = {
                "message": UserConstant.USER_DATA_NOT_FOUND,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return response


class LogoutView(APIView):
    @authentication
    def post(self, request):
        headers = request.headers
        token = headers.get("Authorization")
        response = Response()
        redis = MasterRedis()
        if token:
            payload = jwt.decode(token, JWT.JWT_SECRET, algorithms=['HS256'])
            user = UserData.objects.filter(id=payload['id']).first()
            if not user:
                response.data = {
                    "message": "Unauthorized",
                }
                return response

            if redis.get_keys(str(user.id) + UserConstant.REDIS_USER_KEY):
                redis.delete_keys(str(user.id) + UserConstant.REDIS_USER_KEY)
                response.data = {
                    "message": "Logged Out",
                    "status": status.HTTP_204_NO_CONTENT,
                }
                return Response(response.data, status=status.HTTP_204_NO_CONTENT)
            else:
                response.data = {
                    "message": "Already Logged Out",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
                return Response(response.data, status=status.HTTP_400_BAD_REQUEST)
        response.data = {
            "message": "Logged Out",
            "status": status.HTTP_204_NO_CONTENT,
        }
        return Response(response.data, status=status.HTTP_204_NO_CONTENT)
