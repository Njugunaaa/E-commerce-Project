from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Custom login view (extends JWT login)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass  # Uses the default JWT login behavior

# Register a new user
@api_view(['POST'])
def register_user(request):
    try:
        data = request.data
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=make_password(data['password'])  # Hash the password
        )
        return Response({"message": f"User {user.username} registered successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
