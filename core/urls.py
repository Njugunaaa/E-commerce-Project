from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import CategoryViewSet, ProductViewSet, CartViewSet
from core.auth_views import CustomTokenObtainPairView, register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ✅ API Router Setup
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)  # ✅ API URL for categories
router.register(r'products', ProductViewSet)  # ✅ API URL for products
router.register(r'cart', CartViewSet)
# ✅ Register URLs
urlpatterns = [
    path('api/', include(router.urls)),  # ✅ All API endpoints start with /api/
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register_user, name='register_user'),
]
