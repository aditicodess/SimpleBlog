from django.db import models
from django.utils.html import format_html


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="category/")
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(
                self.image
            )
        )

    class Meta:
        db_table = "category"
        ordering = ["-add_date"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
