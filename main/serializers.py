from rest_framework import serializers
from rest_framework.renderers import JSONRenderer




from .models import Category,Comment,Movie


class MovieSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    content = serializers.CharField()
    category_id=serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.content = validated_data.get("content", instance.content)
        instance.category_id=validated_data.get("category_id",instance.category_id)
        instance.save()
        return instance



class CommentSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    author = serializers.CharField(max_length=50)
    category_id=serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get("author", instance.author)
        instance.category_id=validated_data.get("category_id",instance.category_id)
        instance.save()
        return instance

