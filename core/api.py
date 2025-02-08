from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# API View for Categories
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # ✅ Fetches all categories
    serializer_class = CategorySerializer  # ✅ Uses CategorySerializer

# API View for Products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # ✅ Fetches all products
    serializer_class = ProductSerializer  # ✅ Uses ProductSerializer
 