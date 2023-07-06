from .serializer import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.shortcuts import redirect, render, HttpResponseRedirect


# Register Api
class Register(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'payload': serializer.errors, 'status': 400, 'message': 'Something went Wrong'})
        serializer.save()
        return redirect('Login')


class Login(APIView):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error':'Please provide both the password and username', 'status': 400})

        user = authenticate(request,username=username,password=password)

        if not user:
            return Response({'error': 'invalid Credential', 'status': 404})
        token_obj,created = Token.objects.get_or_create(user=user)
        request.session['username'] = username
        request.session['token'] = str(token_obj)
        
        if Login.return_url:
            return HttpResponseRedirect(Login.return_url)
        else:
            Login.return_url = None
            return redirect('home')