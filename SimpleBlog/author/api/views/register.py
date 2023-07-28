from author.api.serializers.authorModelSerializer import AuthorModelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from author.api.swagger.register_detail import (
    response200,
    response404,
)


class Register(APIView):
    @swagger_auto_schema(
        operation_description="Register a User",
        responses={200: response200, 404: response404},
    )
    def get(self, request):
        return render(request, "register.html")

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title"],
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING,
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                ),
            },
        ),
        operation_description="Register a User",
        responses={200: response200, 404: response404},
    )
    def post(self, request):
        serializer = AuthorModelSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "payload": serializer.errors,
                    "status": 400,
                    "message": "Something went Wrong",
                }
            )
        serializer.save()
        user = User.objects.get(username=serializer.data["username"])
        token_obj, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "payload": serializer.data,
                "token": str(token_obj),
                "status": 200,
                "message": "user logged in",
            }
        )
        # return redirect("Login")
