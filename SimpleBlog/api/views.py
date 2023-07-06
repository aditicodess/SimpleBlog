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
from django.core.paginator import Paginator

class ViewList(APIView):
    def get(self,request):
        blogs = Post.objects.all()
        paginator = Paginator(blogs, 4)
        page_num = request.GET.get('page')
        BlogData = paginator.get_page(page_num)
        totalPage = BlogData.paginator.num_pages
        serializer = PostSerializer(BlogData, many=True)

        data = []
        for info in serializer.data:
            post = {'id': info["id"], 'title': info["title"], 'content':info["content"]}
            data.append(post)
            
        res = {
            'data': data,
            'blogData': BlogData, 
            'lastPage' : totalPage, 
            'totalPageList' : [n+1 for n in range(totalPage)],
            'length': len(data)
        }
        return render(request, "index.html", res)


class AddPost(APIView):
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
        serializer.save()
        return redirect('home')

    def get(self,request):
        return render(request, "create.html")
        

class PostDetails(APIView):
   
    def get(self,request,pk):
        try:
            blog= Post.objects.get(id= pk)
            serializer = PostSerializer(blog)
            data = {
                'title' : serializer.data["title"],
                'description' : serializer.data["description"],
                'id' : serializer.data["id"]
            }
            
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