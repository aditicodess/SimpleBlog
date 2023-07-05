from django.urls import path
from . import views
from middlewares.auth import auth_middleware

urlpatterns = [
    path('',views.ViewList.as_view(), name='home'),
    path('add',auth_middleware(views.AddPost.as_view()),name='Add_List'),
    path('details/<str:pk>',views.PostDetails.as_view(), name='post_details'),
    # path('detail/<str:pk>',views.PostDetails.as_view(), name='post_detail'),
    path('about/', views.AboutDetail.as_view(), name='about')
]