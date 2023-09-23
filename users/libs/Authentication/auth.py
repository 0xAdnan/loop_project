from datetime import datetime

import jwt

from users.libs.redis.redis import MasterRedis
from users.models import UserData
from users.libs.Constants.constants import UserConstant
from rest_framework.response import Response
from rest_framework import status
from lms.libs.constant.constants import JWT


def authentication(function):
    def wrapper(self, request, *args, **kwargs):
        response = Response()
        redis = MasterRedis()
        token = request.headers.get("Authorization")
        if token:
            try:

                payload = jwt.decode(token, JWT.JWT_SECRET, algorithms=['HS256'])

                user = UserData.objects.filter(id=payload['id']).first()

                key = str(user.id) + UserConstant.REDIS_USER_KEY

                if redis.get_keys(key):
                    return function(self, request)
                else:
                    response.data = {
                        "message": "Unauthorized",
                        "status": status.HTTP_400_BAD_REQUEST,
                    }

                    return Response(response.data, status=status.HTTP_400_BAD_REQUEST)

            except Exception:
                response.data = {
                    "message": "Bad Request",
                    "status": status.HTTP_400_BAD_REQUEST,
                }
                return Response(response.data, status=status.HTTP_400_BAD_REQUEST)
        else:

            response.data = {
                "message": "Unauthorized",
                "status": status.HTTP_400_BAD_REQUEST,
            }
            return Response(response.data, status=status.HTTP_400_BAD_REQUEST)

    return wrapper
