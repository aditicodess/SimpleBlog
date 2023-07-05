from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# register user

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        password_hash=User.objects.create_user(username=validated_data['username'])
        password_hash.set_password(validated_data['password'])
        password_hash.save()
        Token.objects.create(user=password_hash)
        return password_hash