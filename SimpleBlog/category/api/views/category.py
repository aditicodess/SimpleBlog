from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.serializers.postModelSerializer import PostModelSerializer
from category.api.serializers.categoryModelSerializer import CategoryModelSerializer
from blog.models import PostModel
from category.models import CategoryModel
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from category.api.swagger.category_detail import (
    category_param_config,
    id_param_config,
    response200,
    response401,
    response404,
)


class AddCategory(APIView):
    @swagger_auto_schema(
        operation_description="GET ALL THE CATEGORIES",
        responses={200: response200, 401: response401, 404: response404},
    )
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategoryModelSerializer(categories, many=True).data
        return Response({"status": 200, "data": serializer})

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title"],
            properties={
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING, default="Programming"
                ),
                "description": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the description about the programming category of the blogs",
                ),
                "image": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the url of the image of the blogs",
                ),
            },
        ),
        operation_description="GET A FORM FOR CREATING POST",
        responses={200: response200, 401: response401, 404: response404},
    )
    def post(self, request):
        serializer = CategoryModelSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "payload": serializer.errors,
                    "status": 400,
                    "message": "Something went Wrong",
                }
            )
        serializer.save()
        # return redirect('view_post')
        return Response({"status": 200, "data": serializer.data})


class CategoryDetails(APIView):
    @swagger_auto_schema(
        operation_description="GET A CATEGORY OF THE BLOG",
        manual_parameters=[id_param_config],
        responses={200: response200, 401: response401, 404: response404},
    )
    def get(self, request, pk):
        try:
            category = CategoryModel.objects.get(id=pk)
            blogs = PostModel.objects.filter(cat=pk)
            serializer = PostModelSerializer(blogs, many=True).data
            serializer2 = CategoryModelSerializer(category).data

            res = {
                "blogs": serializer,
                "category": serializer2,
            }
            return Response({"status": 200, "data": res})
        except ObjectDoesNotExist:
            return Response({"status": 404, "message": "Not Found"})

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title"],
            properties={
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING, default="Programming"
                ),
                "description": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the description about the programming category of the blogs",
                ),
                "image": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the url of the image of the blogs",
                ),
            },
        ),
        operation_description="UPADATE A CATEGORY OF THE BLOG",
        manual_parameters=[id_param_config],
        responses={200: response200, 401: response401, 404: response404},
    )
    def patch(self, request, pk):
        try:
            category = CategoryModel.objects.get(id=pk)
            serializer = CategoryModelSerializer(
                category, data=request.data, partial=True
            )
            if not serializer.is_valid():
                return Response(
                    {
                        "payload": serializer.errors,
                        "status": 400,
                        "message": "Something went Wrong",
                    }
                )
            serializer.save()
            return Response(
                {
                    "payload": serializer.data,
                    "status": 201,
                    "message": "Category is successfully Updated",
                }
            )
        except ObjectDoesNotExist:
            return Response({"status": 404, "message": "Not Found"})

    @swagger_auto_schema(
        operation_description="DELETE A CATEGORY OF THE BLOG",
        manual_parameters=[id_param_config],
        responses={200: response200, 401: response401, 404: response404},
    )
    def delete(self, request, pk):
        try:
            blog = CategoryModel.objects.get(id=pk)
            blog.delete()
            return Response({"message": "Category successfully Deleted", "status": 200})

        except ObjectDoesNotExist:
            return Response({"status": 404, "message": "Not Found"})


class AboutDetail(APIView):
    def get(self, request):
        return render(request, "about.html")
