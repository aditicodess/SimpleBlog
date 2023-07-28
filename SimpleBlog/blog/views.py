# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializer import PostModelSerializer, CategoryModelSerializer
# from .models import PostModel, CategoryModel
# from django.shortcuts import render, redirect
# from rest_framework.views import APIView
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator
# from django.core.paginator import Paginator

# class ViewPost(APIView):
#     def get(self,request):
#         blogs = PostModel.objects.all()
#         paginator = Paginator(blogs, 4)
#         page_num = request.GET.get('page')
#         BlogData = paginator.get_page(page_num)
#         totalPage = BlogData.paginator.num_pages
#         serializer = PostModelSerializer(BlogData, many=True)

#         data = []
#         # print(serializer.data)
#         for info in serializer.data:
#             post = {'id': info["id"], 'title': info["title"], 'content':info["content"]}
#             # print(post)
#             data.append(post)
            
#         res = {
#             'data': data,
#             'blogData': BlogData, 
#             'lastPage' : totalPage, 
#             'totalPageList' : [n+1 for n in range(totalPage)],
#             'length': len(data)
#         }
#         return render(request, "index.html", res)


# class AddPost(APIView):
    
#     def get(self,request):
#         return render(request, "create.html")
        

# class PostDetails(APIView):
   
#     def get(self,request,pk):
#         try:
#             blog= PostModel.objects.get(id= pk)
#             serializer = PostModelSerializer(blog)
#             data = {
#                 'title' : serializer.data["title"],
#                 'description' : serializer.data["description"],
#                 'id' : serializer.data["id"],
#             }
#             print(data)
#             return render(request, "details.html", data)
#         except ObjectDoesNotExist:
#             return Response({'status': 404, 'message': 'Not Found'})

#     @method_decorator(auth_middleware)

#     def post(self,request):
#         info = {
#             # 'by_user' :  request.session.get('username'),
#             'csrfmiddlewaretoken' : request.data.get('csrfmiddlewaretoken'),
#             'title' : request.data.get('title'),
#             'content' : request.data.get('content'),
#             'description' : request.data.get('description'),
#             'cat' : request.data.get('cat')
#         }
#         serializer=PostModelSerializer(data=info)
#         # print('you are: ', request.session.get('username'))
#         if not serializer.is_valid():
#             return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
#         serializer.save()
#         return redirect('view_post')
#         # return Response(serializer.data)

#     def patch(self,request,pk):
#         try:
#             blog = PostModel.objects.get(id=pk)
#             serializer=PostModelSerializer(blog,data=request.data,partial=True)
#             if not serializer.is_valid():
#                 return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
#             serializer.save()
#             return Response({'payload':serializer.data,'status':201,'message':'Blog is successfully Updated'})
#         except ObjectDoesNotExist:
#             return Response({'status': 404, 'message': 'Not Found'})

#     def delete(self,request,pk):
#         try:
#             blog = PostModel.objects.get(id=pk)
#             blog.delete()
#             return Response({'message':'Blog successfully Deleted', 'status':200})

#         except ObjectDoesNotExist:
#             return Response({'status': 404, 'message': 'Not Found'})
        
    
# class AddCategory(APIView):
    
#     def get(self,request):
#         return render(request, "create_category.html")


# class CategoryDetails(APIView):
   
#     def get(self,request,cat):
#         try:
#             blogs = PostModel.objects.get(cat=cat)
#             paginator = Paginator(blogs, 4)
#             page_num = request.GET.get('page')
#             BlogData = paginator.get_page(page_num)
#             totalPage = BlogData.paginator.num_pages
#             serializer = PostModelSerializer(BlogData, many=True)

#             data = []
#             # print(serializer.data)
#             for info in serializer.data:
#                 post = {'id': info["id"], 'title': info["title"], 'content':info["content"]}
#                 # print(post)
#                 data.append(post)
                
#             res = {
#                 'data': data,
#                 'blogData': BlogData, 
#                 'lastPage' : totalPage, 
#                 'totalPageList' : [n+1 for n in range(totalPage)],
#                 'length': len(data)
#             }
#             return render(request, "category_list.html", res)
#         except ObjectDoesNotExist:
#             return Response({'status': 404, 'message': 'Not Found'})

#     @method_decorator(auth_middleware)

#     def post(self,request):
#         serializer=CategoryModelSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
#         serializer.save()
#         # return redirect('view_post')
#         return Response(serializer.data)

#     def patch(self,request,pk):
#         try:
#             category = CategoryModel.objects.get(id=pk)
#             serializer=CategoryModelSerializer(category, data=request.data, partial=True)
#             if not serializer.is_valid():
#                 return Response({'payload':serializer.errors,'status':400,'message':'Something went Wrong'})
#             serializer.save()
#             return Response({'payload':serializer.data,'status':201,'message':'Category is successfully Updated'})
#         except ObjectDoesNotExist:
#             return Response({'status': 404, 'message': 'Not Found'})

#     def delete(self,request,pk):
#         try:
#             blog = CategoryModel.objects.get(id=pk)
#             blog.delete()
#             return Response({'message':'Category successfully Deleted', 'status':200})

#         except ObjectDoesNotExist:
#             return Response({'status': 404, 'message': 'Not Found'})
        

# class AboutDetail(APIView):
#     def get(self,request):
#         return render(request, "about.html")