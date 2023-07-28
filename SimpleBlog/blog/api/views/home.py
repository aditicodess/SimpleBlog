import asgiref
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.serializers.postModelSerializer import PostModelSerializer
from category.api.serializers.categoryModelSerializer import CategoryModelSerializer
from blog.models import PostModel
from category.models import CategoryModel
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.core.paginator import Paginator
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from asgiref.sync import async_to_sync
from blog.api.swagger.post_detail import (
    response200Home,
    response401,
    response404,
)


class ViewPost(APIView):
    @swagger_auto_schema(
        operation_description="GET ALL THE BLOGS AND CATEGORIES",
        responses={200: response200Home, 401: response401, 404: response404},
    )
    def get(self, request):
        blogs = PostModel.objects.all()
        categories = CategoryModel.objects.all()
        serializer = PostModelSerializer(blogs, many=True).data
        # print(serializer)
        serializer2 = CategoryModelSerializer(categories, many=True).data
        res = {
            "blogs": serializer,
            "categories": serializer2,
        }
        return Response({"status": 200, "data": res})
