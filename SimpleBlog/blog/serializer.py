# from rest_framework import serializers
# from .models import PostModel, CategoryModel

# class PostModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= PostModel
#         fields= ('cat', 'title', 'description', 'content', 'date_posted',)

#     def validate_title(self, value):
#         if value != 'this is the title':
#             raise serializers.ValidationError('Provide a valid title name')
#         return value
    
# class CategoryModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= CategoryModel
#         fields= ('cat_id', 'title', 'description', 'add_date',)

#     def validate_title(self, value):
#         if value != 'this is the title':
#             raise serializers.ValidationError('Provide a valid title name')
#         return value