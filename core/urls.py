from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import CategoryViewSet, ProductViewSet
from core.auth_views import register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ✅ API Router Setup
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)  # ✅ API URL for categories
router.register(r'products', ProductViewSet)  # ✅ API URL for products

# ✅ Register URLs
urlpatterns = [
    path('api/', include(router.urls)),  # ✅ All API endpoints start with /api/
    path('register/', register_user, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
