from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.api.serializers.postModelSerializer import PostModelSerializer
from blog.models import PostModel
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.core.paginator import Paginator
from blog.api.swagger.post_detail import (
    id_param_config,
    response200,
    response401,
    response404,
)


class AddPost(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="GET A FORM FOR CREATING POST",
        responses={200: response200, 401: response401, 404: response404},
    )
    def get(self, request):
        return render(request, "create.html")

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title"],
            properties={
                "cat": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    default="Category id of the post",
                ),
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="How to write API's in django",
                ),
                "description": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the main body of the blog",
                ),
                "content": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the short description of the blog",
                ),
                "image": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the url of the image of the blogs",
                ),
            },
        ),
        operation_description="CREATE A POST",
        responses={200: response200, 401: response401, 404: response404},
    )
    def post(self, request):
        print(request.data)
        user = request.data["author"]
        author = User.objects.get(username=user)
        print(request.data["author"])
        print(author.id)
        request.data["author"] = author.id
        serializer = PostModelSerializer(data=request.data)
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


class PostDetails(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="GET DETAILS OF A BLOG",
        manual_parameters=[id_param_config],
        responses={200: response200, 401: response401, 404: response404},
    )
    def get(self, request, pk):
        try:
            blog = PostModel.objects.get(id=pk)
            serializer = PostModelSerializer(blog)
            # data = {
            #     "title": serializer.data["title"],
            #     "description": serializer.data["description"],
            # }
            return Response({"status": 200, "data": serializer.data})
        except ObjectDoesNotExist:
            return Response({"status": 404, "message": "Not Found"})

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title"],
            properties={
                "cat": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    default="Category id of the post",
                ),
                "title": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="How to write API's in django",
                ),
                "description": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the main body of the blog",
                ),
                "content": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the short description of the blog",
                ),
                "image": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="This is the url of the image of the blogs",
                ),
            },
        ),
        operation_description="UPDATE A BLOG",
        manual_parameters=[id_param_config],
        responses={200: response200, 401: response401, 404: response404},
    )
    def patch(self, request, pk):
        try:
            blog = PostModel.objects.get(id=pk)
            serializer = PostModelSerializer(blog, data=request.data, partial=True)
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
                    "message": "Blog is successfully Updated",
                }
            )
        except ObjectDoesNotExist:
            return Response({"status": 404, "message": "Not Found"})

    @swagger_auto_schema(
        operation_description="DELETE A BLOG",
        manual_parameters=[id_param_config],
        responses={200: response200, 401: response401, 404: response404},
    )
    def delete(self, request, pk):
        try:
            blog = PostModel.objects.get(id=pk)
            blog.delete()
            return Response({"message": "Blog successfully Deleted", "status": 200})

        except ObjectDoesNotExist:
            return Response({"status": 404, "message": "Not Found"})


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "put"]
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    pagination_class = None


# class DocumentCreateView(APIView):
#     def post(self, request):
#         serializer = DocumentModelSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(
#                 {
#                     "payload": serializer.errors,
#                     "status": 400,
#                     "message": "Something went Wrong",
#                 }
#             )
#         serializer.save()
#         # return redirect('view_post')
#         return Response({"status": 200, "data": serializer.data})


def download(request, document_id):
    document = get_object_or_404(PostModel, pk=document_id)
    response = HttpResponse(document.image, content_type="image/*")
    response["Content-Disposition"] = f'attachment; filename="{document.image.name}"'
    return response


# import asyncio
# import time
# import aiohttp
# import requests

# async def get_pokemon(session, url):
#     async with session.get(url) as res:
#         pokemon_data = await res.json()
#         return pokemon_data


# async def example(request):

#     starting_time = time.time()

#     actions = []
#     pokemon_data = []

#     async with aiohttp.ClientSession() as session:
#         for num in range(1, 101):
#             url = f"https://pokeapi.co/api/v2/pokemon/{num}"
#             actions.append(asyncio.ensure_future(get_pokemon(session, url)))

#         pokemon_res = await asyncio.gather(*actions)
#         for data in pokemon_res:
#             pokemon_data.append(data)

#     count = len(pokemon_data)
#     total_time = time.time() - starting_time

#     return render(
#         request,
#         "index.html",
#         {"data": pokemon_data, "count": count, "time": total_time},
#     )
