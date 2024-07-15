from rest_framework import serializers
from sales_network.models import Link, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        if 'debt' in validated_data:
            raise serializers.ValidationError({'debt': 'поле не может быть изменено', })
        return super().update(instance, validated_data)

    class Meta:
        model = Link
        fields = '__all__'
