# permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsAdvertisementOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.advertisement.owner == request.user

class IsRentRequestOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsSenderOrRecipient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.recipient == request.user
    
class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Allow access if the user is the owner of the object OR an admin/staff
    """
    def has_object_permission(self, request, view, obj):
        return (
            obj.owner == request.user or
            request.user.is_staff or
            request.user.is_superuser
        )