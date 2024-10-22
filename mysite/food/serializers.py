from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'user_name', 'item_name', 'item_desc', 'item_price', 'item_image']
