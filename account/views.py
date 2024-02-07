from django.shortcuts import render

# Create your views here.
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import CustomUser
from .serializers import SignUpSerializer
from django.shortcuts import get_object_or_404


class SignUpView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = SignUpSerializer
    queryset = CustomUser.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        data = request.data
        serializer = self.serializer_class(user, data=data)
        if serializer.is_valid():
            serializer.save()
            message = {"message": "user updated successfully", "data": serializer.data}
            return Response(data=message, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            message = {"message": "user created successfully", "data": serializer.data}
            return Response(data=message, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.http_400)

    def get(self, request: Request):
        users = CustomUser.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
