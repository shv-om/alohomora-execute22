from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, Authenticate_infoSerializer

from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


# Register API
# class RegisterAPI(generics.GenericAPIView):
#     # serializer_class = RegisterSerializer
#     serializer_class = RegisterSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # auth_info = serializer.pop('authenticate_info')
#         user = serializer.save()
#         print("User: ->", UserSerializer(user, context=self.get_serializer_context()).data)
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "authenticate_info": Authenticate_infoSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)[1]
#             })

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # auth_info = serializer.pop('authenticate_info')
        user, auth = serializer.save()
        # print("User: ->", UserSerializer(user, context=self.get_serializer_context()).data)
        # print("Auth info:", Authenticate_infoSerializer(auth, context=self.get_serializer_context()).data)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "authenticate_info": Authenticate_infoSerializer(auth, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
            })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
