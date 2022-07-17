from rest_framework import serializers
from .models import Mobile

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = (
            'id', 'title', 'description', 'gallery',
            'production_date', 'size', 'panel', 'ram',
            'cpu', 'storage', 'camera', 'slefi_camera',
            'price', 'operating_system'
        )