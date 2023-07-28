from django.contrib import admin
from category.models import CategoryModel
from datetime import date
from django.utils.translation import gettext_lazy as _


class DecadeCategoryAddedListFilter(admin.SimpleListFilter):
    title = _("Category Post decade")
    parameter_name = "decade"

    def lookups(self, request, model_admin):
        return [
            ("10s", _("in the ones")),
            ("20s", _("in the twenties")),
        ]

    def queryset(self, request, queryset):
        if self.value() == "10s":
            return queryset.filter(
                add_date__gte=date(2010, 1, 1),
                add_date__lte=date(2019, 12, 31),
            )
        if self.value() == "20s":
            return queryset.filter(
                add_date__gte=date(2020, 1, 1),
                add_date__lte=date(2029, 12, 31),
            )


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("image_tag", "id", "upper_case_title", "description", "add_date")
    search_fields = ("title",)
    list_filter = [DecadeCategoryAddedListFilter]

    @admin.display(description="Category Title")
    def upper_case_title(self, obj):
        return f"{obj.title}".upper()
