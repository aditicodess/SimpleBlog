from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import PostSerializer
from api.models import Post
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class ViewList(APIView):
    def get(self,request):
        blog=Post.objects.all()
        serializer = PostSerializer(blog,many=True)
        # return Response({'status':201,'payload':serializer.data})
        data = []
        # print({'post':serializer.data})
        
        for info in serializer.data:
            post = {'id': info["id"], 'title': info["title"], 'content':info["content"]}
            data.append(post)
            
        # print(data[1])
        # print(len(data))
        return render(request, "index.html", {'data': data, 'length': len(data)})


class AddPost(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
        serializer.save()
        return redirect('home')
        # return Response({'payload':serializer.data,'status':201,'message':'Blog is created'})

    def get(self,request):
        return render(request, "create.html")
        

class PostDetails(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        try:
            blog= Post.objects.get(id= pk)
            serializer = PostSerializer(blog)
            data = {
                'title' : serializer.data["title"],
                'description' : serializer.data["description"],
                'id' : serializer.data["id"]
            }
            # print({'post':serializer.data["title"]})
            # return Response({'payload':serializer.data, 'status':200})
            return render(request, "details.html", data)
        except ObjectDoesNotExist:
            return Response({'status': 404, 'message': 'Not Found'})

    @method_decorator(auth_middleware)
    def patch(self,request,pk):
        try:
            blog = Post.objects.get(id=pk)
            serializer=PostSerializer(blog,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
            serializer.save()
            return Response({'payload':serializer.data,'status':201,'message':'Blog is successfully Updated'})
        except ObjectDoesNotExist:
            return Response({'status': 404, 'message': 'Not Found'})

    def delete(self,request,pk):
        try:
            blog = Post.objects.get(id=pk)
            blog.delete()
            return Response({'message':'Blog successfully Deleted', 'status':200})

        except ObjectDoesNotExist:
            return Response({'status': 404, 'message': 'Not Found'})
        
    
class AboutDetail(APIView):
    def get(self,request):
        return render(request, "about.html")