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
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .tokens import create_jwt_pair_for_user


class SignUpView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request):
        print("posting............................")
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {"message": "user created successfully", "data": serializer.data}
            return Response(data=message, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        print("signing in......................")
        email = request.data.get("email")
        password = request.data.get("password")
        print("email:", email)
        print("password:", password)
        user = authenticate(email=email, password=password)
        print("user....................", user)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message": "loge in successful",
                "tokens": tokens,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(
            data={"message": "invalid user"}, status=status.HTTP_401_UNAUTHORIZED
        )

    def get(self, request: Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(data=content, status=status.HTTP_200_OK)
