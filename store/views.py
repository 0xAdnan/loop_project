from django.shortcuts import render

# Create your views here.

from rest_framework.views import  APIView
from rest_framework import status
import logging
from rest_framework.response import Response
from store.serializers.serializerStore import StatusSerializer
from store.serializers.serializerStore import BusinessHourSerializer
from store.serializers.serializerStore import TimeZoneSerializer


class AddStoreStatus(APIView):
    def post(self, request):
        response = Response()
        print("REQUEST DATA", request.data)
        data = {
            "store_status" : None,
        "timestamp_utc" : None,
        "store_id": None
        }
        print("DATA ===> ", request.data.get("store_status"))
        data['store_status'] = request.data.get("store_status")
        data['timestamp_utc'] = request.data.get("timestamp_utc")
        data['store_id'] = request.data.get("store_id")
        print("STORE DATA ===>", data)
        serializer_store_status = StatusSerializer(data = data)
        serializer_store_status.is_valid()

        if serializer_store_status.is_valid():
            obj_store_status = serializer_store_status.save()
            response.data = {
                "message":"Status saved successfully",
                "data" : serializer_store_status.data
            }
            response.status_code = status.HTTP_200_OK
        else:
            response.data = {
                "message": "Error",
            }
            response.status_code = status.HTTP_400_BAD_REQUEST
        return response

class AddStoreBusinessHours(APIView):
    def post(self, request):
        response = Response()
        print("REQUEST DATA", request.data)
        data = {
            "store_id": None,
            "day_of_week": None,
            "start_time_local": None,
            "end_time_local": None
        }
        print("DATA ===> ", request.data.get("store_id"))
        data['store_id'] = request.data.get("store_id")
        data['day_of_week'] = request.data.get("day_of_week")
        data['start_time_local'] = request.data.get("start_time_local")
        data['end_time_local'] = request.data.get("end_time_local")
        print("STORE DATA ===>", data)

        # Create the serializer instance
        serializer_business_hour = BusinessHourSerializer(data=data)

        # Check if the serializer is valid
        if serializer_business_hour.is_valid():
            # Save the object and retrieve it if needed
            obj_store_status = serializer_business_hour.save()

            response.data = {
                "message": "Status saved successfully",
                "data": serializer_business_hour.data
            }
            response.status_code = status.HTTP_200_OK
        else:
            response.data = {
                "message": "Error",
            }
            response.status_code = status.HTTP_400_BAD_REQUEST
        return response

class AddStoreTimeZone(APIView):
    def post(self, request):
        response = Response()
        print("REQUEST DATA", request.data)
        data = {
            "store_id": None,
            "timezone_str": None
        }
        print("DATA ===> ", request.data.get("store_id"))
        data['store_id'] = request.data.get("store_id")
        data['timezone_str'] = request.data.get("timezone_str")
        print("STORE DATA ===>", data)

        # Create the serializer instance
        serializer_timezone = TimeZoneSerializer(data=data)

        # Check if the serializer is valid
        if serializer_timezone.is_valid():
            # Save the object and retrieve it if needed
            obj_store_status = serializer_timezone.save()

            response.data = {
                "message": "Status saved successfully",
                "data": serializer_timezone.data
            }
            response.status_code = status.HTTP_200_OK
        else:
            response.data = {
                "message": "Error",
            }
            response.status_code = status.HTTP_400_BAD_REQUEST
        return response