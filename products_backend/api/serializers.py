from rest_framework import serializers
from .models import Product


# PUBLIC_INTERFACE
class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model with basic validation rules."""

    class Meta:
        model = Product
        fields = ("id", "name", "price", "quantity", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_price(self, value):
        """Ensure price is non-negative."""
        if value < 0:
            raise serializers.ValidationError("Price must be non-negative.")
        return value

    def validate_quantity(self, value):
        """Ensure quantity is non-negative."""
        if value < 0:
            raise serializers.ValidationError("Quantity must be non-negative.")
        return value
