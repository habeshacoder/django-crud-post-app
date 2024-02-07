from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "spouse_name", "username", "password"]


def validate(self, attr):

    email_exists = CustomUser.objects.filter(email=attr["email"]).exists()
    if email_exists:
        raise ValidationError("email has already been used")
    return super.validate(attr)


def create(self, validated_data):
    password = validated_data.pop("password")
    user = super.create(validated_data)
    user.set_password(password)
    user.save()
    Token.objects.create(user=user)
    return user
