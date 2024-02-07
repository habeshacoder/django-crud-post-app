from django.shortcuts import render

# Create your views here.
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import CustomUser
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, APIView


class SignUpView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {"message": "user created successfully", "data": serializer.data}
            return Response(data=message, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.http_400)


class SignInView(APIView)
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            response = {
                "message": "loge in successful",
                "data": user.auth_token.key,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(
            data={"message": "invalid user"}, status=status.HTTP_401_UNAUTHORIZED
        )
