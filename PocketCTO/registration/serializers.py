from rest_framework import serializers, fields
from django.contrib.auth.models import User

from . import models
from securityModule.secureAuth import secureAuth

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)

class Authenticate_infoSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = models.Authenticate_info
        fields = ['dob', 'image']

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    authenticate_info = Authenticate_infoSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'authenticate_info')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        auth_info = validated_data.pop('authenticate_info')
        passwd = validated_data['password']
        dob = auth_info['dob']

        SA = secureAuth()
        newpass = SA.getEffectivePass(passwd, dob)

        user = User.objects.create_user(validated_data['username'], validated_data['email'], newpass,)
        auth = models.Authenticate_info.objects.create(user=user, **auth_info)

        return (user, auth)
