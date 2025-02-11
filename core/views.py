from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order, Category
from .serializers import ProductSerializer, OrderSerializer, CategorySerializer, CartSerializer
from .permissions import IsAdminUser, IsSellerOrReadOnly

# ✅ Product Management View
class ProductViewSet(viewsets.ModelViewSet):
    """
    Allows sellers to manage their own products.
    Admins can manage all products.
    Buyers can only view products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Ensure only logged-in users can access
    def get_permissions(self):
        """Set permissions based on user role"""
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsSellerOrReadOnly]  # Sellers can create/edit/delete their products
        else:
            self.permission_classes = [IsAuthenticated]  # All users can view products
        return super().get_permissions()

    def perform_create(self, serializer):
        """Assign the logged-in user as the product seller"""
        serializer.save(seller=self.request.user)

# ✅ Order Management View
class OrderViewSet(viewsets.ModelViewSet):
    """
    Allows buyers to place orders.
    Admins can manage all orders.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        """Set permissions based on user role"""
        if self.action in ['list', 'retrieve', 'update', 'destroy']:
            self.permission_classes = [IsAdminUser]  # Only admins can view/manage orders
        else:
            self.permission_classes = [IsAuthenticated]  # Buyers can place orders
        return super().get_permissions()

    def perform_create(self, serializer):
        """Assign the logged-in user as the order owner"""
        serializer.save(user=self.request.user)

# ✅ Category Management View (Admin Only)
class CategoryViewSet(viewsets.ModelViewSet):
    """
    Admins can manage categories.
    Buyers and sellers can only view categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        """Set permissions based on user role"""
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAdminUser]  # Only admins can modify categories
        else:
            self.permission_classes = [IsAuthenticated]  # Buyers and sellers can view categories
        return super().get_permissions()

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Show only items in the logged-in user's cart"""
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Assign the logged-in user to the cart item"""
        serializer.save(user=self.request.user)