from rest_framework import serializers
from ..models import StatusTimeStampt
from ..models import BusinessHoursTime
from ..models import TimezonesDetails
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTimeStampt
        fields = ['id', 'store_id', 'timestamp_utc', 'store_status']


class BusinessHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessHoursTime
        fields = ['id', 'store_id', 'day_of_week', 'start_time_local', 'end_time_local']

class TimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimezonesDetails
        fields = ['id', 'store_id', 'timezone_str']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
