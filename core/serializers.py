from rest_framework import serializers
from .models import Category, Product

# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # ✅ Includes all fields in the JSON output

# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # ✅ Shows full category details in JSON

    class Meta:
        model = Product
        fields = '__all__'  # ✅ Includes all fields in the JSON output
 