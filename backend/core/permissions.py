from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Custom permission to give full control to admin users.
    """

    def has_permission(self, request, view):
        # Allow access only if the user is an admin
        return request.user and request.user.is_staff
