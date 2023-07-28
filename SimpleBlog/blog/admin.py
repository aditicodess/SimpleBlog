from django.contrib import admin
from blog.models import PostModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "cat",
        "description",
        "decade_post_in",
    )
    list_filter = [
        "author",
        ("title", admin.EmptyFieldListFilter),
    ]
    actions = ["make_published"]
    readonly_fields = ("date_posted",)
    search_fields = ("title",)
    list_per_page = 50

    @admin.action(description="Mark selected post as published")
    def make_published(self, request, queryset):
        queryset.update(status="p")

    class Media:
        js = ("/static/placeholder.js",)
