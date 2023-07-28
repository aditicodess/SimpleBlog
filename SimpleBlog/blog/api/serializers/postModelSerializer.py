from rest_framework import serializers
from author.api.serializers.authorModelSerializer import AuthorModelSerializer
from category.api.serializers.categoryModelSerializer import CategoryModelSerializer
from category.models import CategoryModel
from blog.models import PostModel
from django.core.files import File
import base64
from drf_extra_fields.fields import Base64ImageField
from django.core.files.base import ContentFile
import uuid


class PostModelSerializer(serializers.ModelSerializer):
    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = (
            "id",
            "cat",
            "author",
            "title",
            "description",
            "content",
            "image",
            "base64_image",
            "date_posted",
        )

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

    def to_representation(self, instance):
        rep = super(PostModelSerializer, self).to_representation(instance)
        rep["cat"] = instance.cat.title
        rep["author"] = instance.author.username
        return rep

    # def to_internal_value(self, data):
    #     data = data.split(",")[-1]
    #     print(data)
    #     decoded_data = base64.b64decode(data)
    #     filename = str(uuid.uuid4()) + ".jpg"
    #     image_file = ContentFile(decoded_data, name=filename)
    #     return super().to_internal_value(image_file)
