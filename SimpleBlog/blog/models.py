from django.db import models
from category.models import CategoryModel
from django.contrib.auth.models import User
from django.contrib import admin
import uuid
import os

STATUS = [
    ("d", "Drafted"),
    ("p", "Published"),
]


# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to="downloads/")
#     uploaded_at = models.DateTimeField(auto_now_add=True)


class PostModel(models.Model):
    author = models.ForeignKey(
        User,
        default="",
        on_delete=models.CASCADE,
        related_query_name="post_by_user",
        related_name="post_by_user",
        verbose_name="By User",
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.CharField(max_length=200)
    date_posted = models.DateField(auto_now_add=True)
    cat = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/", null=True)
    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post"
        ordering = ["-date_posted"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    @admin.display(description="Post decade")
    def decade_post_in(self):
        decade = self.date_posted.year // 10 * 10
        return f"{decade}’s"

    @staticmethod
    def get_post_by_id(ids):
        return PostModel.objects.filter(id=ids)

    @staticmethod
    def get_post_by_userid(ids):
        return PostModel.objects.filter(author=ids)

    @staticmethod
    def get_all_posts():
        return PostModel.objects.all()

    @staticmethod
    def get_all_posts_by_categoryid(category_id):
        if category_id:
            return PostModel.objects.filter(cat=category_id)
        else:
            return PostModel.get_all_products()
