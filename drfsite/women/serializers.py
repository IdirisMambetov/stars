from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = "__all__"


# class WomanModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

    # title = serializers.CharField(max_length=200)
    # content = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # cat_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Women.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.content = validated_data.get("content", instance.content)
    #     instance.time_update = validated_data.get("time_published", instance.time_update)
    #     instance.is_published = validated_data.get("is_published", instance.is_published)
    #     instance.cat_id = validated_data.get("cat_id", instance.cat_id)
    #     instance.save()
    #     return instance



# def encode():
#     model = WomanModel('Andjelina Jolie', 'Content: Andjelina Jolie')
#     model_sr = WomanSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)