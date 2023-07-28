from django.http import HttpResponseRedirect

# from author.api.models.author import AuthorModel
from author.api.serializers.authorModelSerializer import AuthorModelSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from django.views import View
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import redirect, render


class Login(ObtainAuthToken):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get("return_url")
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response(
                {
                    "error": "Please provide both the password and username",
                    "status": 400,
                }
            )

        user = authenticate(request, username=username, password=password)
        print(user)
        if not user:
            return Response({"error": "invalid Credential", "status": 404})
        token_obj, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "status": 200,
                "data": str(user),
                "token": str(token_obj),
                "massage": "your are successfully logged in",
            }
        )
        # email = request.data.get("email")
        # author = AuthorModel.objects.filter(email=email).first()
        # password = request.data.get("password")

        # if email is None or password is None:
        #     return Response(
        #         {
        #             "error": "Please provide both the password and username",
        #             "status": 400,
        #         }
        #     )

        # if author:
        #     flag = check_password(password, author.password)
        #     # print(flag)
        #     if flag:
        #         request.session["user"] = author.id
        #         request.session["email"] = author.email
        #         if Login.return_url:
        #             return HttpResponseRedirect(Login.return_url)
        #         else:
        #             Login.return_url = None
        #             return Response(
        #                 {
        #                     "status": 200,
        #                     "message": "user logged in",
        #                 }
        #             )
        #             # return redirect("view_post")
        #     else:
        #         return Response(
        #             {"error": "Email or Password invalid !!", "status": 404}
        #         )
        # else:
        #     return Response({"error": "invalid Credential", "status": 404})
