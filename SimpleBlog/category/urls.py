from django.urls import path
from category.api.views.category import CategoryDetails, AddCategory, AboutDetail

# from middlewares.auth import auth_middleware

urlpatterns = [
    path("categories", AddCategory.as_view(), name="add_category"),
    path("category/<str:pk>", CategoryDetails.as_view(), name="category_details"),
    path("about/", AboutDetail.as_view(), name="about_detail"),
]
