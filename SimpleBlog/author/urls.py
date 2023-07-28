from django.urls import path
from author.api.views.register import Register
from author.api.views.login import Login

# from middlewares.auth import auth_middleware

urlpatterns = [
    path("register/", Register.as_view(), name="Register"),
    path("login/", Login.as_view(), name="Login"),
]
