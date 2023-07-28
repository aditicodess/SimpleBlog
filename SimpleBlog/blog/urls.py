from django.urls import path
from blog.api.views.post import download
from blog.api.views.post import PostDetails, AddPost
from blog.api.views.home import ViewPost

# from middlewares.auth import auth_middleware

urlpatterns = [
    path("", ViewPost.as_view(), name="view_post"),
    path("add_post", AddPost.as_view(), name="add_post"),
    path("post/<str:pk>", PostDetails.as_view(), name="post_details"),
    # path("upload/", DocumentCreateView.as_view(), name="upload"),
    path("download/<int:document_id>/", download, name="download"),
]
