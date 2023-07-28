from rest_framework import serializers

# from author.api.models.author import AuthorModel
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    # def validate(self, customer):
    #     print(customer.get("username"))
    #     if not customer.get("username"):
    #         raise serializers.ValidationError("UserName Required !!")
    #     elif len(customer.get("username")) < 4:
    #         raise serializers.ValidationError("UserName must be 4 char long or more")
    #     elif len(customer.get("password")) < 6:
    #         raise serializers.ValidationError("Password must be 6 char long")
    #     else:
    #         return customer
