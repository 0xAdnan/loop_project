from rest_framework import serializers
from .models import UserData
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id', 'first_name', 'last_name', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
#
#
# class LogoutSerializer(serializers.Serializer):
#     refresh = serializers.CharField()
#
#     default_error_messages = {
#         "bad_token": 'Token is expired or invalid'
#     }
#
#     def validate(self, attrs):
#         print("Attribute", attrs)
#         self.token = attrs.get("refresh")
#         return attrs
#
#     def save(self, **kwargs):
#         try:
#             RefreshToken(self.token).blacklist()
#         except TokenError:
#             self.fail("bad_token")
