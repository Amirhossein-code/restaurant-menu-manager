from rest_framework import serializers
from ..models import Item


class ItemSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            "id",
            "title",
            "unit_price",
            "category",
            "slug",
            "available",
            "description",
            "image",
        ]
        read_only_fields = ["id", "slug"]

    # def get_image(self, obj):
    #     if obj.image:
    #         original_url = obj.image.url
    #         # Construct absolute URL with the current host and port
    #         absolute_url = f"http://{self.context['request'].get_host()}{original_url}"
    #         modified_url = absolute_url.replace(":8000/", ":8001/")
    #         return modified_url
    #     else:
    #         return None


class SimpleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "title",
            "unit_price",
            "category",
            "slug",
        ]
        read_only_fields = ["id", "slug"]
