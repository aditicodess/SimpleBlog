from rest_framework import serializers
from category.models import CategoryModel
import base64
from django.core.files import File


class CategoryModelSerializer(serializers.ModelSerializer):
    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = CategoryModel
        fields = ("title", "id", "description", "image", "base64_image")

    def get_base64_image(self, obj):
        try:
            print(obj.image.url)
            f = open(obj.image.path, "rb")
            imageFile = File(f)
            data = base64.b64encode(imageFile.read())
            f.close()
            return data
        except:
            print(obj.image)
            pass
